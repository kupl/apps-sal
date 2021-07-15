n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

x = y = t = 0
for i in range(n):
    dx, dy, dt = l[i][1], l[i][2], l[i][0]
    dist = abs((dx - x) + (dy - y))

    if abs(dt - t) < dist or (dt - t - dist) % 2:
        print("No")
        return

    x, y, t = dx, dy, dt
print("Yes")
