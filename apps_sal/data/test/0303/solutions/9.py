x1, y1, x2, y2 = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]

dx = abs(x2 - x1)
dy = abs(y2 - y1)

if dx % x != 0 or dy % y != 0:
    print("NO")
else:
    kx = dx // x
    ky = dy // y

    if (kx % 2) == (ky % 2):
        print("YES")
    else:
        print("NO")


