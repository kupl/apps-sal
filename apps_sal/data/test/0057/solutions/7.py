n = int(input())

if n == 1 or n == 0:
    print(-1)
elif n == 2:
    x1, y1 = [int(x) for x in input().split()]
    x2, y2 = [int(x) for x in input().split()]

    if x1 == x2 or y1 == y2:
        print(-1)
    else:
        print(abs((x1 - x2) * (y1 - y2)))
elif n == 3:
    x1, y1 = [int(x) for x in input().split()]
    x2, y2 = [int(x) for x in input().split()]
    x3, y3 = [int(x) for x in input().split()]

    print(abs((max(x1, max(x2, x3)) - min(x1, min(x2, x3))) * (max(y1, max(y2, y3)) - min(y1, min(y2, y3)))))
else:
    x1, y1 = [int(x) for x in input().split()]
    x2, y2 = [int(x) for x in input().split()]
    x3, y3 = [int(x) for x in input().split()]
    x4, y4 = [int(x) for x in input().split()]

    print(abs((max(x1, max(x2, x3)) - min(x1, min(x2, x3))) * (max(y1, max(y2, y3)) - min(y1, min(y2, y3)))))
