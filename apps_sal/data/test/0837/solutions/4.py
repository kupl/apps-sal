def main():
    def f(t):
        u = cache.get(t)
        if u is None:
            if t & 1:
                u = min(f(t - 1), f(t + 1)) + x
            else:
                u = x * t
                if y * 2 < u:
                    u = f(t // 2) + y
            cache[t] = u
        return u

    n, x, y = list(map(int, input().split()))
    cache = {1: x}
    print(f(n))


def __starting_point():
    main()


__starting_point()
