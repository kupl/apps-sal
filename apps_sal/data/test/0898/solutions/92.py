def divisor(n):
    i = 1
    res = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return res


def main():
    (n, m) = map(int, input().split())
    md = list(divisor(m))
    md.sort(reverse=True)
    for i in md:
        if i * n <= m:
            print(i)
            return


def __starting_point():
    main()


__starting_point()
