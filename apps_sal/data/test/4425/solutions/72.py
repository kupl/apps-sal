def main():
    (n, k) = list(map(int, input().split()))
    ans = 0.0
    for t in range(1, n + 1):
        cnt = 0
        now = t
        per = 1.0
        while now < k:
            per /= 2
            now *= 2
        ans += per / n
    print('{:.20}'.format(ans))
    pass


def __starting_point():
    main()


__starting_point()
