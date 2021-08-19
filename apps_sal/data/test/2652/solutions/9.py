from heapq import heappush, heappop, heapify
N = int(input())

X = []
Y = []
for n in range(N):
    x, y = list(map(int, input().split()))
    X.append([x, n])
    Y.append([y, n])  # 座標、頂点番号
X.sort()
Y.sort()

# 隣接リスト。大きさではなく町番号で記録
adj = list([] for _ in range(N))

# 隣接リストを作る
for n in range(N - 1):  # X[n]は下からn番目に大きい数
    costx = X[n + 1][0] - X[n][0]
    # お互いの隣接リストにコストと相手の番号を追加
    adj[X[n + 1][1]].append([costx, X[n][1]])  # コストと相手の番号
    adj[X[n][1]].append([costx, X[n + 1][1]])

    costy = Y[n + 1][0] - Y[n][0]
    adj[Y[n + 1][1]].append([costy, Y[n][1]])  # コストと相手の番号
    adj[Y[n][1]].append([costy, Y[n + 1][1]])


used = [0] * N
que = [(w, c) for w, c in adj[0]]  # コスト,番号
used[0] = 1
heapify(que)
ans = 0
while que:
    cv, v = heappop(que)  # cvはコスト。vは番号
    if used[v]:
        continue
    used[v] = 1
    ans += cv
    for w, c in adj[v]:  # vを追加
        if used[c]:
            continue
        heappush(que, (w, c))
print(ans)
