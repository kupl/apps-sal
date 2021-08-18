def divisors(x):
    def f(y, q):
        t = -len(r)
        while not y % q:
            y //= q
            for i in range(t, 0):
                r.append(r[t] * q)
        return y

    r, p = [1], 7
    x = f(f(f(x, 2), 3), 5)
    while x >= p * p:
        for s in 4, 2, 4, 2, 4, 6, 2, 6:
            if not x % p:
                x = f(x, p)
            p += s
    if x > 1:
        f(x, x)
    return r


def main():
    a, s = int(input()), input()
    if not a:
        z = sum(x * (x + 1) for x in map(len, s.translate(
            str.maketrans('123456789', '         ')).split())) // 2
        x = len(s)
        print((x * (x + 1) - z) * z)
        return
    sums, x, cnt = {}, 0, 1
    for u in map(int, s):
        if u:
            sums[x] = cnt
            x += u
            cnt = 1
        else:
            cnt += 1
    if x * x < a:
        print(0)
        return
    sums[x], u = cnt, a // x
    l = [v for v in divisors(a) if v <= x]
    z = a // max(l)
    d = {x: 0 for x in l if z <= x}
    for x in d:
        for k, v in list(sums.items()):
            u = sums.get(k + x, 0)
            if u:
                d[x] += v * u
    print(sum(u * d[a // x] for x, u in list(d.items())))


def __starting_point():
    main()


__starting_point()
