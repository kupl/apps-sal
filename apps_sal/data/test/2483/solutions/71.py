import sys
sys.setrecursionlimit(10**6)
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62 - 1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, C, STC):
    from collections import Counter
    se = [(2 * s, 0, c) for s, t, c in STC]
    te = [(2 * t + 1, 1, c) for s, t, c in STC]
    e = se + te
    e.sort(reverse=True)
    r = Counter()
    ans = 0
    while e:
        _, k, c = e.pop()
        if k == 0:
            r[c] += 1
        else:
            r[c] -= 1
            if r[c] == 0:
                r.pop(c)
        ans = max(ans, len(r))
    return ans


def main():
    N, C = read_int_n()
    STC = [read_int_n() for _ in range(N)]
    print(slv(N, C, STC))


def __starting_point():
    main()


__starting_point()
