x1, y1, x2, y2 = list(map(int, input().split()))
x, y = list(map(int, input().split()))

x, y = abs(x), abs(y)

x_ = abs(x2 - x1)
y_ = abs(y2 - y1)

if (x == 0 or x_ % x == 0) and (y == 0 or y_ % y == 0):
    if x == 0 or y == 0:
        print("YES")
    if (x_ // x + y_ // y) % 2 == 0:
        print("YES")  # kek
    else:
        print("NO")
else:
    print("NO")
