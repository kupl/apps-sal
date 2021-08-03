import sys
input = sys.stdin.readline
for f in range(int(input())):
    x, y = map(int, input().split())
    c1, c2, c3, c4, c5, c6 = map(int, input().split())
    c2 = min(c2, c1 + c3)
    c5 = min(c5, c4 + c6)
    c6 = min(c6, c1 + c5)
    c3 = min(c3, c2 + c4)

    c1 = min(c1, c2 + c6)
    c4 = min(c4, c3 + c5)
    if x * y > 0:
        if x > 0:
            d = min(x, y)
            x -= d
            y -= d
            print(x * c6 + y * c2 + d * c1)
        else:
            x = -x
            y = -y
            d = min(x, y)
            x -= d
            y -= d
            print(x * c3 + y * c5 + d * c4)
    else:
        cost = 0
        if x > 0:
            cost += x * c6
        else:
            cost -= x * c3
        if y > 0:
            cost += y * c2
        else:
            cost -= y * c5
        print(cost)
