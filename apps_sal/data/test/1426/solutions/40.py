import heapq

N, M = list(map(int, input().split()))

L = [[] for i in range(3 * N)]

for i in range(M):
    u, v = list(map(int, input().split()))
    u, v = u - 1, v - 1
    L[u].append(N + v)
    L[N + u].append(2 * N + v)
    L[2 * N + u].append(v)

S, T = list(map(int, input().split()))

D = [10**6 for i in range(3 * N)]
D[~-S] = 0
A = [(0, ~-S)]
heapq.heapify(A)

while len(A) > 0:
    d, v = heapq.heappop(A)
    if D[v] < d:
        continue
    for i in L[v]:
        if D[i] > D[v] + 1:
            D[i] = D[v] + 1
            heapq.heappush(A, (D[v] + 1, i))

print((D[~-T] // 3 if D[~-T] != 10**6 else -1))
