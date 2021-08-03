for nt in range(int(input())):
    y, x = list(map(int, input().split()))
    c1, c2, c3, c4, c5, c6 = list(map(int, input().split()))
    for i in range(10):
        c2 = min(c2, c1 + c3)
        c3 = min(c3, c2 + c4)
        c4 = min(c4, c3 + c5)
        c5 = min(c5, c4 + c6)
        c6 = min(c6, c5 + c1)
        c1 = min(c1, c6 + c2)
    # print (c1,c2,c3,c4,c5,c6)
    if x >= 0:
        if y >= 0:
            m = min(x, y)
            x -= m
            y -= m
            print(m * c1 + c2 * x + c6 * y)
        else:
            y = abs(y)
            print(x * c2 + y * c3)
    else:
        x = abs(x)
        if y >= 0:
            print(x * c5 + y * c6)
        else:
            y = abs(y)
            m = min(x, y)
            x -= m
            y -= m
            print(m * c4 + x * c5 + y * c3)
