

def get_ints():
    return [int(n) for n in input().split()]


def get_floats():
    return [float(n) for n in input().split()]


def calc(w, rid):
    plus = True
    val = 0
    for i, t in enumerate(w):
        if i not in rid:
            if plus:
                val += t
            else:
                val -= t
            plus = not plus
    return val


def __starting_point():
    a = get_ints()
    assert len(a) == 1
    n = a[0]
    count = 2 * n

    w = get_ints()
    assert len(w) == count
    w.sort(reverse=True)

    best = list()
    for i in range(count):
        for j in range(i + 1, count):
            best.append(calc(w, [i, j]))

    print(min(best))


__starting_point()
