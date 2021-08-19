import sys
from bisect import bisect


def read():
    return sys.stdin.readline().rstrip()


def main():
    (a, b, q) = list(map(int, read().split()))
    s = [-10 ** 12] + [int(read()) for _ in range(a)] + [10 ** 12]
    t = [-10 ** 12] + [int(read()) for _ in range(b)] + [10 ** 12]
    for _ in range(q):
        x = int(read())
        si = bisect(s, x)
        ti = bisect(t, x)
        (sa, sb) = (s[si - 1], s[si])
        (ta, tb) = (t[ti - 1], t[ti])
        d = 10 ** 12
        for sx in (sa, sb):
            for tx in (ta, tb):
                d = min(abs(x - sx) + abs(sx - tx), abs(x - tx) + abs(tx - sx), d)
        print(d)


def __starting_point():
    main()


__starting_point()
