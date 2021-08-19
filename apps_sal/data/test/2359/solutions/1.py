from fractions import Fraction as F


def solve():
    (h, c, t) = map(int, input().split())
    dt = abs(F(h - t))
    ans = 1

    def update(u, v):
        nonlocal dt, ans
        if u <= 0 or v < 0:
            return
        w = F(u * h + v * c, u + v)
        if abs(w - t) < dt:
            dt = abs(w - t)
            ans = u + v
    update(1, 1)
    ax = (h - t) // (2 * t - h - c) if 2 * t - h - c else 0
    for x in range(ax - 3, ax + 4):
        update(x + 1, x)
    print(ans)


t = int(input())
for _ in range(t):
    solve()
