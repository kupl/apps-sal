from numpy import *
(N, M, Q) = map(int, input().split())
G = zeros((N, N), int)
for m in range(M):
    (l, r) = map(int, input().split())
    G[N - l][r - 1] += 1
G = cumsum(cumsum(G, axis=0), axis=1)
for n in range(Q):
    (p, q) = map(int, input().split())
    print(G[N - p][q - 1])
