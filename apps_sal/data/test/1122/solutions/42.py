
def __starting_point():
    nm = input()
    nm = nm.split()
    n = int(nm[0])
    m = int(nm[1])

    if n % 2 == 1:
        for i in range(1, m + 1):
            print((i, n + 1 - i))

    if n % 2 == 0:
        t = n
        f = 0

        for i in range(1, m + 1):
            p = i - 1 + t - n
            if p >= n - i - 1 and f == 0:
                f = 1
                n -= 1
            print((i, n))
            n -= 1


__starting_point()
