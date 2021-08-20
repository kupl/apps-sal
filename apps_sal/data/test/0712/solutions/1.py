def main():
    tmp = input().split()
    (n, p, t) = (int(tmp[0]), float(tmp[1]), int(tmp[2]))
    q = 1.0 - p
    res = [0.0] * (n + 1)
    res[0] = 1.0
    for _ in range(t):
        tmp = [x * q for x in res]
        tmp[-1] = res[-1]
        for i in range(n):
            tmp[i + 1] += res[i] * p
        res = tmp
    print(sum((x * i for (i, x) in enumerate(res))))


def __starting_point():
    main()


__starting_point()
