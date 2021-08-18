def out(t, x1, y1, x2, y2, x3, y3, m):
    if t == 1:
        print(x1)
        for i in range(y1):
            for j in range(x1):
                print("A", end="")
            print()
        for i in range(y2):
            for j in range(x1):
                print("B", end="")
            print()
        for i in range(y3):
            for j in range(x1):
                print("C", end="")
            print()
    else:
        if m == 1:
            print(x1)
            for i in range(y1):
                for j in range(x1):
                    print("A", end="")
                print()
            for i in range(x1 - y1):
                for j in range(x1):
                    if x2 > j:
                        print("B", end="")
                    else:
                        print("C", end="")
                print()
        elif m == 2:
            print(x2)
            for i in range(y2):
                for j in range(x2):
                    print("B", end="")
                print()
            for i in range(x2 - y2):
                for j in range(x2):
                    if x1 > j:
                        print("A", end="")
                    else:
                        print("C", end="")
                print()
        else:
            print(x3)
            for i in range(y3):
                for j in range(x3):
                    print("C", end="")
                print()
            for i in range(x3 - y3):
                for j in range(x3):
                    if x1 > j:
                        print("A", end="")
                    else:
                        print("B", end="")
                print()


def check1(x1, y1, x2, y2, x3, y3):
    a, b = max(x1, y1), min(x1, y1)
    b += (y2 if x2 == a else x2) + (y3 if x3 == a else x3)
    if a == b:
        out(1, a, min(x1, y1), a, (y2 if x2 == a else x2), a, (y3 if x3 == a else x3), 1)
    return a == b


def check2(x1, y1, x2, y2, x3, y3):
    a, b = max(x1, y1), min(x1, y1)
    bt = x2 + x3
    if (bt == a) and (y2 == a - b) and (y3 == a - b):
        out(2, a, b, x2, y2, x3, y3, 1)
        return
    bt = x2 + y3
    if (bt == a) and (y2 == a - b) and (x3 == a - b):
        out(2, a, b, x2, y2, y3, x3, 1)
        return
    bt = y2 + x3
    if (bt == a) and (x2 == a - b) and (y3 == a - b):
        out(2, a, b, y2, x2, x3, y3, 1)
        return
    bt = y2 + y3
    if (bt == a) and (x2 == a - b) and (x3 == a - b):
        out(2, a, b, y2, x2, y3, x3, 1)
        return

    a, b = max(x2, y2), min(x2, y2)
    bt = x1 + x3
    if (bt == a) and (y1 == a - b) and (y3 == a - b):
        out(2, x1, y1, a, b, x3, y3, 2)
        return
    bt = x1 + y3
    if (bt == a) and (y1 == a - b) and (x3 == a - b):
        out(2, x1, y1, a, b, y3, x3, 2)
        return
    bt = y1 + x3
    if (bt == a) and (x1 == a - b) and (y3 == a - b):
        out(2, y1, x1, a, b, x3, y3, 2)
        return
    bt = y1 + y3
    if (bt == a) and (x1 == a - b) and (x3 == a - b):
        out(2, y1, x1, a, b, y3, x3, 2)
        return

    a, b = max(x3, y3), min(x3, y3)
    bt = x2 + x1
    if (bt == a) and (y2 == a - b) and (y1 == a - b):
        out(2, x1, y1, x2, y2, a, b, 3)
        return
    bt = x2 + y1
    if (bt == a) and (y2 == a - b) and (x1 == a - b):
        out(2, y1, x1, x2, y2, a, b, 3)
        return
    bt = y2 + x1
    if (bt == a) and (x2 == a - b) and (y1 == a - b):
        out(2, x1, y1, y2, x2, a, b, 3)
        return
    bt = y2 + y1
    if (bt == a) and (x2 == a - b) and (x1 == a - b):
        out(2, y1, x1, y2, x2, a, b, 3)
        return


x1, y1, x2, y2, x3, y3 = [int(x) for x in input().split()]
b = check1(x1, y1, x2, y2, x3, y3)
if b:
    return
b = check2(x1, y1, x2, y2, x3, y3)
if b:
    return
print(-1)
