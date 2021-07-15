for i in range(int(input())):
    x = input()
    h = len(x)
    f = (int(x) >= int(x[0] * h))
    print((h - 1) * 9 + int(x[0]) - 1 + f)
