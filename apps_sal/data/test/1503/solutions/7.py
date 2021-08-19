def summarize(val):
    return (val + 1) * val // 2


def calc(data):
    m = len(data)
    n = len(data[0])
    reflections = []
    for i in range(m):
        reflections.append(dict())
        r = reflections[-1]
        for j in range(n):
            r[data[i][j]] = j
    lengths = []
    index = 0
    while index < n:
        val = data[0][index]
        ln = 1
        indexes = [reflections[i][val] for i in range(1, m)]
        for k in range(index + 1, n):
            d = k - index
            equal = True
            val = data[0][k]
            for i in range(1, m):
                if indexes[i - 1] + d >= n or data[i][indexes[i - 1] + d] != val:
                    equal = False
                    break
            if equal:
                ln += 1
            else:
                break
        lengths.append(summarize(ln))
        index += ln
    return sum(lengths)


def get_ints():
    return [int(n) for n in input().split()]


def get_floats():
    return [float(n) for n in input().split()]


def seq2str(seq):
    return ' '.join((str(item) for item in seq))


def __starting_point():
    a = get_ints()
    assert len(a) == 2
    (n, m) = (a[0], a[1])
    data = []
    for i in range(m):
        a = get_ints()
        assert len(a) == n
        data.append(a)
    res = calc(data)
    print(res)


__starting_point()
