# WsSc0L
x, y = map(int, input().split())
if y > x and x >= -y:
    print(y * 4 - 2)
elif y < x and x <= -y + 1:
    print(-y * 4)
elif y <= x and x > -y + 1:
    print(x * 4 - 3)
elif y >= x and x < -y:
    print(-1 - 4 * x)
else:
    print(0)
