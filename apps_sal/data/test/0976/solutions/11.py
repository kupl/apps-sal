def main():
    n, x = list(map(int, input().split()))
    tot, t = 0, 1
    for _ in range(n):
        l, r = list(map(int, input().split()))
        t1 = r
        r -= t - 1
        l -= t
        tot += r - l + l % x
        t = t1 + 1
    print(tot)


def __starting_point():
    main()


__starting_point()
