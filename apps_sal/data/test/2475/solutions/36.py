###############################################################################

from sys import stdout
from bisect import bisect_left as binl
from copy import copy, deepcopy
from collections import defaultdict
import math


mod = 1


def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return tuple(map(int, input_tuple))


def intina():
    return [int(i) for i in input().split()]


def intinl(count):
    return [intin() for _ in range(count)]


def modadd(x, y):
    nonlocal mod
    return (x + y) % mod


def modmlt(x, y):
    nonlocal mod
    return (x * y) % mod


def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


def combination(x, y):
    assert(x >= y)

    ret = math.factorial(x)
    ret = ret // (math.factorial(x - y) * math.factorial(y))

    return ret


def get_divisors(x):
    retlist = []
    for i in range(1, int(x**0.5) + 3):
        if x % i == 0:
            retlist.append(i)
            retlist.append(x // i)
    return retlist


def get_factors(x):
    retlist = []
    for i in range(2, int(x**0.5) + 3):
        while x % i == 0:
            retlist.append(i)
            x = x // i
    retlist.append(x)
    return retlist


def make_linklist(xylist):
    linklist = {}
    for a, b in xylist:
        linklist.setdefault(a, [])
        linklist.setdefault(b, [])
        linklist[a].append(b)
        linklist[b].append(a)
    return linklist


def calc_longest_distance(linklist, v=1):
    distance_list = {}
    distance_count = 0
    distance = 0
    vlist_previous = []
    vlist = [v]
    nodecount = len(linklist)

    while distance_count < nodecount:
        vlist_next = []
        for v in vlist:
            distance_list[v] = distance
            distance_count += 1
            vlist_next.extend(linklist[v])
        distance += 1
        vlist_to_del = vlist_previous
        vlist_previous = vlist
        vlist = list(set(vlist_next) - set(vlist_to_del))

    max_distance = -1
    max_v = None
    for v, distance in list(distance_list.items()):
        if distance > max_distance:
            max_distance = distance
            max_v = v

    return (max_distance, max_v)


def calc_tree_diameter(linklist, v=1):
    _, u = calc_longest_distance(linklist, v)
    distance, _ = calc_longest_distance(linklist, u)
    return distance


class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def root(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.root(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        rooti = self.root(i)
        rootj = self.root(j)
        if rooti == rootj:
            return
        if rooti < rootj:
            self.parent[rootj] = rooti
        else:
            self.parent[rooti] = rootj

    def same(self, i, j):
        return self.root(i) == self.root(j)


###############################################################################


def main():
    n = intin()
    alist = intina()

    ans = 0

    for i in range(1, n//2):
        lsum = 0
        for j in range(1, n):
            down = n - i * j - 1
            up = i * j
            if (down <= up and down % i == 0):
                break
            if (down <= i):
                break
            if (n - 1 - up <= i):
                break
            lsum += alist[down]
            lsum += alist[up]
            ans = max(ans, lsum)

    print(ans)


def __starting_point():
    main()

__starting_point()
