def main():
    K = int(input())
    l = []
    for i in range(1, 1000):
        l.append(i)
    for k in range(1, 13):
        n0 = 10 ** k
        for i in range(100, 1000):
            l.append(i * n0 + n0 - 1)
    r = []
    for n in l:
        sn = 0
        d = n
        while 0 < d:
            (d, m) = (int(d / 10), d % 10)
            sn += m
        r.append(n / sn)
    min_r = r[-1]
    for i in range(len(r) - 2, -1, -1):
        if min_r < r[i]:
            r.pop(i)
            l.pop(i)
        else:
            min_r = r[i]
    for i in range(K):
        print(l[i])


def __starting_point():
    main()


__starting_point()
