def __starting_point():

    x = [500, 1000, 1500, 2000, 2500]
    m = [int(x) for x in input().split()]
    w = [int(x) for x in input().split()]
    hs, hu = [int(x) for x in input().split()]

    res = 0
    for i in range(5):
        res += max(3 * x[i] // 10, x[i] - m[i] * x[i] // 250 - 50 * w[i])
    res += 100 * hs
    res -= 50 * hu
    print(res)


__starting_point()
