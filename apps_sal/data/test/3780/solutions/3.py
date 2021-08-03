def f(T):
    t1 = min(t, T)
    t2 = max(T - t, 0)
    u = [v[0] * t1 + w[0] * t2, v[1] * t1 + w[1] * t2]
    C = [A[0] + u[0], A[1] + u[1]]
    dist = ((C[0] - B[0]) ** 2 + (C[1] - B[1]) ** 2) ** 0.5
    dist2 = Vmax * T
    return dist2 >= dist


def read(): return list(map(int, input().split()))


A, B, v, w = [[0, 0] for i in range(4)]
A[0], A[1], B[0], B[1] = read()
Vmax, t = read()
v[0], v[1] = read()
w[0], w[1] = read()
L, R = 0, 1e12
for i in range(100):
    M = (L + R) / 2
    if f(M):
        R = M
    else:
        L = M
ans = R
print(ans)
