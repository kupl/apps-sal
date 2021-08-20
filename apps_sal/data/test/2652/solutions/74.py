from heapq import heappush, heappop, heapify
N = int(input())
A = []
for i in range(N):
    (x, y) = map(int, input().split())
    A.append((x, y, i))
A = sorted(A)
B = sorted(A, reverse=False, key=lambda x: x[1])
E = [[] for i in range(N)]
for i in range(N - 1):
    (x1, x2) = (A[i][2], A[i + 1][2])
    (y1, y2) = (B[i][2], B[i + 1][2])
    E[x1].append((x2, A[i + 1][0] - A[i][0]))
    E[x2].append((x1, A[i + 1][0] - A[i][0]))
    E[y1].append((y2, B[i + 1][1] - B[i][1]))
    E[y2].append((y1, B[i + 1][1] - B[i][1]))
G = E
used = [0] * N
que = [(c, w) for (w, c) in G[0]]
used[0] = 1
heapify(que)
ans = 0
while que:
    (cv, v) = heappop(que)
    if used[v]:
        continue
    used[v] = 1
    ans += cv
    for (w, c) in G[v]:
        if used[w]:
            continue
        heappush(que, (c, w))
print(ans)
