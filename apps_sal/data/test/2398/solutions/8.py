for q in range(int(input())):
    l, r, d, u = [int(i) for i in input().split()]
    x, y, x1, y1, x2, y2 = [int(i) for i in input().split()]
    if (l + r > 0 and x1 == x2) or (u + d > 0 and y1 == y2):
        print("No")
        continue
    x += r - l
    y += u - d
    if (x >= x1 and x <= x2 and y >= y1 and y <= y2):
        print("Yes")
    else:
        print("No")
