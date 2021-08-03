import heapq
import sys
input = sys.stdin.readline

N, Q = list(map(int, input().split()))
AB = [tuple(map(int, input().split())) for _ in range(N)]
CD = [tuple(map(int, input().split())) for _ in range(Q)]
H = 2 * 10**5  # 幼稚園

INF = 10**18
rates = [[] for _ in range(H)]
members = [set() for _ in range(H)]
belongs = [-1] * N
for i, (a, b) in enumerate(AB):
    b -= 1
    heapq.heappush(rates[b], (-a, i))
    members[b].add(i)
    belongs[i] = b

mxrates = []
for num, r in enumerate(rates):
    if len(r) > 0:
        heapq.heappush(mxrates, (-r[0][0], num))  # 幼稚園ごとの最大値をいれる

for c, d in CD:
    c, d = c - 1, d - 1
    old = belongs[c]
    belongs[c] = d
    members[old].remove(c)
    members[d].add(c)
    # 転園元の最大値を最新化する
    while len(rates[old]) > 0 and rates[old][0][1] not in members[old]:
        heapq.heappop(rates[old])
    # 最新化された転園元から改めて取得
    if len(rates[old]) > 0:
        heapq.heappush(mxrates, (-rates[old][0][0], old))
    # 転園先に追加
    heapq.heappush(rates[d], (-AB[c][0], c))
    heapq.heappush(mxrates, (AB[c][0], d))
    while mxrates:
        rate, num = mxrates[0]
        # mxratesの最小が最新ではない場合
        if len(rates[num]) == 0 or -rates[num][0][0] != rate:
            heapq.heappop(mxrates)
        else:
            print(rate)
            break
