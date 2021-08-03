def gcd(a, b):
    while(b != 0):
        a %= b
        t = a
        a = b
        b = t
    return a


def main():
    a, b = list(map(int, input().split(' ')))
    gg = gcd(a, b)
    ans = 0
    can = 1
    A = []
    A.append(a / gg)
    A.append(b / gg)
    for g in A:
        while(g != 1):
            ok = 0
            if g % 2 == 0:
                g = g / 2
                ok = 1
                ans = ans + 1
            if g % 3 == 0:
                g = g / 3
                ok = 1
                ans = ans + 1
            if g % 5 == 0:
                g = g / 5
                ok = 1
                ans = ans + 1
            if ok == 0:
                can = 0
                break

    if can == 0:
        print("-1")
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
