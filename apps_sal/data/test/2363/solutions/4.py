for i in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    s = 0
    if a > 0:
        s = b // a
        a, b = b - s * a, a
        while a > 0:
            k = b // a
            a, b = b - k * a, a
            s += k
    print(s)
