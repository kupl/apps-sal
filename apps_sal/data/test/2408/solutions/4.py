import itertools
import math
from functools import reduce
from math import gcd
gcdm = lambda *args: reduce(gcd, args, 0)


def pointsToLine2d(p1, p2):
    if p1 == p2:
        return (0, 0, 0)
    (_p1, _p2) = sorted((p1, p2))
    g = gcdm(*[x for x in (_p2[1] - _p1[1], _p1[0] - _p2[0], _p1[1] * _p2[0] - _p1[0] * _p2[1]) if x != 0])
    return ((_p2[1] - _p1[1]) // g, (_p1[0] - _p2[0]) // g, (_p1[1] * _p2[0] - _p1[0] * _p2[1]) // g)


def dist(p1, p2):
    return sum(((a - b) * (a - b) for (a, b) in zip(p1, p2))) ** 0.5


def pointsToLines(p1, p2):
    return list(map(pointsToLine2d, itertools.combinations(p1, 2), itertools.combinations(p2, 2)))


def areParallel(l1, l2):
    return l1[0] * l2[1] == l2[0] * l1[1]


def areSame(l1, l2):
    return areParallel(l1, l2) and l1[1] * l2[2] == l2[1] * l1[2]


def collinear(p1, p2, p3):
    return areSame(pointsToLine2d(p1, p2), pointsToLine2d(p2, p3))


def intersect(l1, l2):
    return None if areParallel(l1, l2) else ((l2[1] * l1[2] - l1[1] * l2[2]) / (l2[0] * l1[1] - l1[0] * l2[1]), (l1[0] * l2[2] - l1[2] * l2[0]) / (l2[0] * l1[1] - l1[0] * l2[1]))


def rotate(p, theta, origin=(0, 0)):
    return (origin[0] + (p[0] - origin[0]) * math.cos(theta) - (p[1] - origin[1]) * math.sin(theta), origin[1] + (p[0] - origin[0]) * math.sin(theta) + (p[1] - origin[1]) * math.cos(theta))


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
        stdout.write(sep.join((str(a) for a in args)) + end)

    def write_array(array, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join((str(a) for a in array)) + end)
    n = read_int()
    p = []
    for _ in range(n):
        p.append(read_int_array())
    lines = set()
    for i in range(n):
        for j in range(i + 1, n):
            lines.add(pointsToLine2d(p[i], p[j]))
    k = len(lines)
    import collections
    ax_bx = collections.defaultdict(int)
    out = 0
    for (a, b, _) in lines:
        ax_bx[a, b] += 1
    for x in list(ax_bx.values()):
        out += (k - x) * x
    write(out // 2)


main()
