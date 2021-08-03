def main():
    n, a, b = list(map(int, input().split()))

    s = 6 * n

    if a * b >= s:
        print(a * b)
        print(a, b)
        return

    ma, mb = min(a, b), max(a, b)

    _s = float('inf')
    _a = 0

    for i in range(min(int(s**0.5) + 1, s // mb), ma - 1, -1):
        _b = (s + i - 1) // i
        si = i * _b
        if _s > si:
            _a, _s = i, si
            if si == s:
                break
    print(_s)
    _b = _s // _a
    if not (a <= _a and b <= _b):
        _a, _b = _b, _a
    print(_a, _b)


def __starting_point():
    main()


__starting_point()
