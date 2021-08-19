def main():
    (n, m) = list(map(int, input().split()))
    (lo, hi) = (1, n)
    for _ in range(m):
        (u, v) = list(map(int, input().split()))
        if u > v:
            if lo < v:
                lo = v
            if hi > u:
                hi = u
        else:
            if lo < u:
                lo = u
            if hi > v:
                hi = v
    print(max(hi - lo, 0))


def __starting_point():
    main()


__starting_point()
