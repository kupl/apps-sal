def f():
    return map(int, input().split())


(N, K) = f()
(*A,) = list(f())
F = [-1] * (2 * 10 ** 5 + 1)
G = []
n = 1
while F[n] == -1:
    F[n] = len(G)
    G.append(n)
    n = A[n - 1]
t = len(G) - F[n]
l = F[n]
if l <= K:
    K -= l
    K %= t
    K += l
print(G[K])
