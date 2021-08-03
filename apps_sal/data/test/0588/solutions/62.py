def solve():
    from math import atan2, degrees, hypot
    n = int(input())
    txy = []
    sx, sy = 0, 0
    for i in range(n):
        a, b = list(map(int, input().split()))
        theta_0 = degrees(atan2(b, a))
        sx += a
        sy += b
        txy.append([theta_0, a, b])
    txy.sort()
    ans = hypot(sx, sy)
    for i in range(n):
        for j in range(i + 1, n):
            tx, ty = 0, 0
            for k in range(i, j):
                theta, x, y = txy[k]
                tx += x
                ty += y
                ans = max(ans, hypot(tx, ty))
                ans = max(ans, hypot(sx - tx, sy - ty))
    print(ans)


solve()
