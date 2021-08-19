def main():
    n = int(input())
    m = b = 0
    for (k, a) in sorted((tuple(map(int, input().split())) for _ in range(n))):
        if k - m > 15:
            b = 1 if b else 0
        else:
            r = 4 ** (k - m)
            b = (b + r - 1) // r
        if b < a:
            b = a
        m = k
    if b == 1:
        k += 1
    else:
        r = 1
        while r < b:
            r *= 4
            k += 1
    print(k)


def __starting_point():
    main()


__starting_point()
