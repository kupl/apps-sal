from functools import reduce
from math import gcd
import collections

gcdm = lambda *args: reduce(gcd, args, 0)


def pointsToLine2d(p1, p2):
    if p1 == p2:
        return 0, 0, 0
    p1, p2 = sorted((p1, p2))
    a, b, c = p2[1] - p1[1], p1[0] - p2[0], p1[1] * p2[0] - p1[0] * p2[1]
    g = gcdm(*[x for x in (a, b, c) if x != 0])
    return a // g, b // g, c // g


def main():
    from sys import stdin, stdout

    def read():
        return stdin.readline().rstrip('\n')

    def read_array(sep=None, maxsplit=-1):
        return read().split(sep, maxsplit)

    def read_int():
        return int(read())

    def read_int_array(sep=None, maxsplit=-1):
        return [int(a) for a in read_array(sep, maxsplit)]

    def write(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in args) + end)

    def write_array(array, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in array) + end)

    n = read_int()
    p = []
    for _ in range(n):
        p.append(read_int_array())

    lines = set()
    for i in range(n):
        for j in range(i + 1, n):
            lines.add(pointsToLine2d(p[i], p[j]))

    k = len(lines)
    ax_bx = collections.defaultdict(int)
    out = 0
    for a, b, _ in lines:
        ax_bx[a, b] += 1
    for x in list(ax_bx.values()):
        out += (k - x) * x
    write(out // 2)


main()
