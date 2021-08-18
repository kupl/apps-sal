from heapq import *

N, M, S = list(map(int, input().split()))

T = [[10**18 for _ in range(2451)] for _ in range(N)]

act = [[] for _ in range(N)]

for i in range(M):
    U, V, A, B = list(map(int, input().split()))
    U -= 1
    V -= 1
    act[U] += [(V, A, B)]
    act[V] += [(U, A, B)]

for i in range(N):
    C, D = tuple(map(int, input().split()))
    act[i] += [(i, -C, D)]

que = [(0, 0, S)]

while que:
    (currentT, n, coins) = heappop(que)
    for m, cost, t in act[n]:
        if coins >= cost and currentT + t < T[m][min(2450, coins - cost)]:
            T[m][min(2450, coins - cost)] = currentT + t
            heappush(que, (currentT + t, m, min(2450, coins - cost)))

for i in range(1, N):
    print((min(T[i])))
