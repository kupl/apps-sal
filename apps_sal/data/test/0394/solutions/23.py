

def check(d, length):
    n = len(d)
    t = d[:length]
    for i, item in enumerate(d):
        if t[i % length] != item:
            return False
    return True


def calc(a):
    k = []
    d = []
    last = 0
    for item in a:
        d.append(item - last)
        last = item
    for i in range(len(a)):
        if check(d, i + 1):
            k.append(i + 1)

    return k


def get_ints():
    return [int(n) for n in input().split()]


def get_floats():
    return [float(n) for n in input().split()]


def seq2str(seq):
    return ' '.join(str(item) for item in seq)


def __starting_point():
    a = get_ints()
    assert len(a) == 1
    n = a[0]
    a = get_ints()
    assert len(a) == n

    k = calc(a)
    print(len(k))
    print(seq2str(k))


__starting_point()
