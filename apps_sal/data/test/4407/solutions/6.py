

DEGREE_ARRAY_SIZE = 32


def convert(a):
    from collections import Counter
    b = [0 for i in range(DEGREE_ARRAY_SIZE)]
    for val, cnt in list(Counter(a).items()):
        b[val.bit_length() - 1] += cnt
    start = 0
    for i, cnt in enumerate(reversed(b)):
        if cnt != 0:
            start = DEGREE_ARRAY_SIZE - i
            break
    return b, start


def calc(q, b):
    ans = 0
    val_power = (len(b) - 1)
    for cnt in reversed(b):
        c = min(cnt, q >> val_power)
        q -= c * (1 << val_power)
        ans += c
        val_power -= 1

    return ans if q == 0 else -1


def get_ints():
    return [int(n) for n in input().split()]


def get_floats():
    return [float(n) for n in input().split()]


def __starting_point():
    a = get_ints()
    assert len(a) == 2
    n, q = a[0], a[1]
    a = get_ints()
    assert len(a) == n

    b, start = convert(a)
    b = b[:start]
    DEGREE_ARRAY_SIZE = start

    q = [int(input()) for _ in range(q)]
    for i in q:
        ans = calc(i, b)
        print(ans)


__starting_point()
