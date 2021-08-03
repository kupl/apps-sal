W, H, N = map(int, input().split())
u, U, v, V = 0, W, 0, H
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        u = max(u, x)
    if a == 2:
        U = min(U, x)
    if a == 3:
        v = max(v, y)
    if a == 4:
        V = min(V, y)


def f(x): return x if x > 0 else 0


print(f(U - u) * f(V - v))
