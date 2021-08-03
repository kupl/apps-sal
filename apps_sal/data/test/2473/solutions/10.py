def main():
    n, k, *xy = list(map(int, open(0).read().split()))
    _x_ = sorted(xy[::2])
    ans = 4 * 10 ** 18
    for _x in _x_:
        for x_ in _x_[1:]:
            w = x_ - _x
            c = 0
            _h_ = []
            for x, y in zip(xy[::2], xy[1::2]):
                if _x <= x <= x_:
                    c += 1
                    _h_.append(y)

            if c >= k:
                _h_.sort()
                h = min(_h_[i + k - 1] - _h_[i] for i in range(c - k + 1))
                ans = min(ans, h * w)

    print(ans)


def __starting_point():
    main()


__starting_point()
