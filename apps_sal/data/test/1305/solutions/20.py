def f():
    n = int(input())
    t = list(map(int, input().split()))
    (a, b) = (0, 0)
    for i in t:
        if i == 25:
            a += 1
        elif i == 50:
            b += 1
            a -= 1
        elif b > 0:
            b -= 1
            a -= 1
        else:
            a -= 3
        if a < 0:
            return 1
    return 0


print('YNEOS'[f()::2])
