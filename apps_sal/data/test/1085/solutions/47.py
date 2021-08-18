def main():
    N = int(input())

    def divisor_set(x):
        ret = set()
        if x > 1:
            ret.add(x)

        d = 2
        while d * d <= x:
            if x % d == 0:
                ret.add(d)
                ret.add(x // d)
            d += 1
        return ret

    ans = 0
    ans += len(divisor_set(N - 1))

    for k in divisor_set(N):
        x = N
        while x % k == 0:
            x //= k
        if x % k == 1:
            ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()
