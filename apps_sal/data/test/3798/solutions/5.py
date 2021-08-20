def main():
    (n, s) = (int(input()), int(input()))
    if n < s:
        print(-1)
        return
    if n == s:
        print(n + 1)
        return
    for b in range(2, int(n ** 0.5) + 1):
        (x, sb) = (n, 0)
        while 0 < x:
            sb += x % b
            x //= b
        if sb == s:
            print(b)
            return
    for p in range(1, int(n ** 0.5) + 1)[::-1]:
        if (n - s) % p:
            continue
        (b, x, sb) = ((n - s) // p + 1, n, 0)
        while 0 < x:
            sb += x % b
            x //= b
        if sb == s:
            print(b)
            return
    print(-1)


def __starting_point():
    main()


__starting_point()
