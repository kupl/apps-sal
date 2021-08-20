(N, K) = map(int, input().split())
A = list(map(int, input().split()))
G = [1]
for n in range(N - 1):
    G.append(A[G[n] - 1])
if len(G) < K:
    a = G.index(G[-1])
    b = len(G) - a - 1
    K = (K - a) % b + a
print(G[K])
