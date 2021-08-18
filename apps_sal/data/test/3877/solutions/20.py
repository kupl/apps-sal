import sys


def read_input():
    for idx, line in enumerate(sys.stdin):
        if idx == 0:
            return (int(x) for x in line.strip().split(' '))


def count_all(n):
    if len(n) == 0:
        return 0
    else:
        return 2 * count_all(n[:-1]) + 1


def count_ones(n):
    if len(n) == 0:
        return 0
    else:
        return 2 * count_ones(n[:-1]) + int(n[-1])


def process_rec(n, l, r):
    if r - l > count_all(n):
        assert False
    if r - l == count_all(n):
        return count_ones(n)
    else:
        l_count = r_count = count_all(n[:-1])
        m_count = int(n[-1])
        res = 0

        if l < l_count:
            res += process_rec(n[:-1], l, min(r, l_count))
        if l <= l_count and r > l_count:
            res += m_count
        if r > l_count + 1:
            res += process_rec(n[:-1], max(l - l_count - 1, 0), r - l_count - 1)

        return res


def process(n, l, r):
    n = "{0:b}".format(n)
    return process_rec(n, l - 1, r)


def print_output(res):
    print(res)


def __starting_point():
    print_output(process(*read_input()))


__starting_point()
