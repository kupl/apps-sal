def num_denied(a, b, groups):
    c = 0
    d = 0
    for g in groups:
        if g == 1:
            if a > 0:
                a -= 1
            elif b > 0:
                b -= 1
                c += 1
            elif c > 0:
                c -= 1
            else:
                d += 1
        elif g == 2:
            if b > 0:
                b -= 1
            else:
                d += 2
    return d


def __starting_point():
    n, a, b = list(map(int, input().split()))
    groups = list(map(int, input().split()))
    print(num_denied(a, b, groups))


__starting_point()
