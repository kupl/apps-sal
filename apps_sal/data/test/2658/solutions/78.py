def f():
    return map(int, input().split())


(N, K) = f()
(*A,) = list(f())
F = [-1] * (2 * 10 ** 5 + 1)
G = []
i = 1
while F[i] == -1:
    F[i] = len(G)
    G.append(i)
    i = A[i - 1]
t = F[i]
if K < t:
    print(G[K])
else:
    G = G[t:]
    print(G[(K - t) % len(G)])
