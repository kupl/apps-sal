def NoW(xs):
    if sum(xs) % 3 != 0:
        return 0
    else:
        part = sum(xs) // 3
        ci = ret = 0
        acum = xs[0]
        for (i, x) in enumerate(xs[1:]):
            if acum == 2 * part:
                ret += ci
            if acum == part:
                ci += 1
            acum += x
        return ret


input()
xs = list(map(int, input().split()))
print(NoW(xs))
