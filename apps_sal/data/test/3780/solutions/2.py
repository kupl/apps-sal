x, y, a, b = map(int, input().split())
a -= x
b -= y
v, t = map(int, input().split())
vx, vy = map(int, input().split())
ux, uy = map(int, input().split())


def ok(T):
    U = max(0, T - t)
    V = min(t, T)
    X = a - U * ux - V * vx
    Y = b - U * uy - V * vy
    return X * X + Y * Y <= ((U + V) * v)**2


l = 0
r = 1e9
while r - l > 1e-6:
    m = (l + r) / 2
    if ok(m): r = m
    else: l = m
print(r)
