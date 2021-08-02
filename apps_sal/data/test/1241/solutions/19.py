mx = 0


def f(need, c, k, n):
    for i in range(n):
        if i + need - 1 >= n:
            break
        temp = c[i + need - 1]
        if i > 0:
            temp -= c[i - 1]
        if temp + k >= need:
            return (True, i)

    return (False, None)


def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    c = [0 for i in range(n)]

    c[0] = a[0]

    for i in range(1, n):
        c[i] = c[i - 1]
        if a[i] == 1:
            c[i] += 1

    l, r = k, n + 1

    while r - l > 100:
        m = (l + r) // 2
        if f(m, c, k, n)[0]:
            l = m
        else:
            r = m

    for i in range(r, l - 1, -1):
        res, start = f(i, c, k, n)
        if res:
            print("%d" % i)
            print((" ".join(str(x)
                            for x in a[:start] + [1] * i + a[start + i:])))
            return


def __starting_point():
    main()
    # print(gcd(100, 2))


__starting_point()
