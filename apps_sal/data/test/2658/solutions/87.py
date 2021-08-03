def f(): return map(int, input().split())


N, K = f()
*A, = list(f())

F = [0] * (2 * 10**5 + 1)

G = [1]
F[1] = 1
i = 0
while i <= N:
    new = A[G[-1] - 1]
    if F[new] == 1:
        break
    F[new] = 1
    G.append(new)
    i += 1
t = G.index(A[G[-1] - 1])
if (K < t):
    print(G[K])
else:
    G = G[t:]
    print(G[(K - t) % len(G)])
