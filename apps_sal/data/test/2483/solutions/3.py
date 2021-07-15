def main():
    from itertools import accumulate
    n, c, *stc = list(map(int, open(0).read().split()))
    table = [0] * 2 * (10 ** 5 + 1)
    m = list(zip(stc[::3], stc[1::3], stc[2::3]))
    m.sort(key=lambda a: (a[2], a[0], a[1]))

    ch_ = 0
    t_ = 0
    for s, t, ch in m:
        if ch != ch_:
            ch_ = ch
            t_ = 0
        if t_ == 2 * s:
            table[t_ + 1] += 1
        else:
            table[2 * s - 1] += 1

        table[2 * t + 1] -= 1
        t_ = 2 * t

    *x, = accumulate(table)
    ans = max(x)

    print(ans)


def __starting_point():
    main()

__starting_point()
