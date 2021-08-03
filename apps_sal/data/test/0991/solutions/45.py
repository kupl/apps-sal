import heapq
n, m, s = map(int, input().split())
rail = [[] for _ in range(n)]
fare = [[] for _ in range(n)]
time = [[] for _ in range(n)]
rate = []
TIME = []
for _ in range(m):
    i, j, k, l = map(int, input().split())
    i -= 1
    j -= 1
    rail[i].append(j)
    rail[j].append(i)
    fare[i].append(k)
    fare[j].append(k)
    time[i].append(l)
    time[j].append(l)
for _ in range(n):
    i, j = map(int, input().split())
    rate.append(i)
    TIME.append(j)

# Dijkstra's algorithm
# 銀貨の枚数がlimit以上になったら捨てる
limit = [max(i) for i in fare]
limit = max(limit) * n
if s >= limit:
    s = limit - 1

# dp[i][j] = 都市iで銀貨j枚を持っているための必要最小時間
dp = [[float('inf')] * limit for _ in range(n)]

# candidateに(必要時間, 都市番号, 銀貨の枚数)を追加していく
candidate = [(0, 0, s)]
heapq.heapify(candidate)

ans = [-1] * n
todo = n

while todo > 0:
    i, j, k = heapq.heappop(candidate)
    if dp[j][k] != float('inf'):
        continue
    dp[j][k] = i
    if ans[j] == -1:
        ans[j] = i
        todo -= 1

    # 鉄道移動をcandidateに追加
    for l in range(len(rail[j])):
        if fare[j][l] <= k and dp[rail[j][l]][k - fare[j][l]] == float('inf'):
            heapq.heappush(candidate, (i + time[j][l], rail[j][l], k - fare[j][l]))

    # 両替をcandidateに追加
    if k < limit - 1:
        heapq.heappush(candidate, (i + TIME[j], j, min([k + rate[j], limit - 1])))

for i in range(1, n):
    print(ans[i])
