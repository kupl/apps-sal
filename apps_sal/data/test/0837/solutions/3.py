def main():
    def f(t):
        if t & 1:
            return x if t == 1 else min(f(t - 1), f(t + 1)) + x
        else:
            u = x * t
            return f(t // 2) + y if y * 2 < u else u

    n, x, y = list(map(int, input().split()))
    print(f(n))


def __starting_point():
    main()


__starting_point()
