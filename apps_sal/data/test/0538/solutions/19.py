def get_ints():
    return [int(n) for n in input().split()]


def get_floats():
    return [float(n) for n in input().split()]


def __starting_point():
    a = get_ints()
    assert len(a) == 1
    x = a[0]
    s = str(x).rstrip('0')
    print('YES' if s == s[::-1] else 'NO')


__starting_point()
