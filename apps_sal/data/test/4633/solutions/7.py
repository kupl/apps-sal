for _ in range(int(input())):
    (a, b) = map(int, input().split())
    bb = b
    can = 0
    d = 10000000000000000000
    while d > 0:
        bb = bb - a // d % 10
        d = d // 10
    if bb >= 0:
        can = 1
    d = 10000000000000000000
    t = 0
    while d > 0 and b - a // d % 10 >= 1:
        b = b - a // d % 10
        t = (a // d + 1) * d
        d = d // 10
    if can:
        print(0)
    else:
        print(t - a)
    t = 0
