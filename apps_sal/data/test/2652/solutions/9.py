from heapq import heappush, heappop, heapify
N = int(input())

X = []
Y = []
for n in range(N):
    x, y = list(map(int, input().split()))
    X.append([x, n])
    Y.append([y, n])
X.sort()
Y.sort()

adj = list([] for _ in range(N))

for n in range(N - 1):
    costx = X[n + 1][0] - X[n][0]
    adj[X[n + 1][1]].append([costx, X[n][1]])
    adj[X[n][1]].append([costx, X[n + 1][1]])

    costy = Y[n + 1][0] - Y[n][0]
    adj[Y[n + 1][1]].append([costy, Y[n][1]])
    adj[Y[n][1]].append([costy, Y[n + 1][1]])


used = [0] * N
que = [(w, c) for w, c in adj[0]]
used[0] = 1
heapify(que)
ans = 0
while que:
    cv, v = heappop(que)
    if used[v]:
        continue
    used[v] = 1
    ans += cv
    for w, c in adj[v]:
        if used[c]:
            continue
        heappush(que, (w, c))
print(ans)
