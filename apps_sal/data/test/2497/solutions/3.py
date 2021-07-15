import bisect
import heapq
import sys


input = sys.stdin.readline
sys.setrecursionlimit(100000)


class V:
    def __init__(self, f):
        self.f = f
        self.v = None

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n)

    def get(self):
        return self.v


def read_values():
    return list(map(int, input().split()))


def read_list():
    return list(read_values())


def calc_v(D, f, i):
    p, n, c = V(f), V(f), V(f)
    for d, P in list(D.items()):
        for pp in P:
            if d == ("R" if i == 0 else "U"):
                p.ud(pp[i])
            elif d == ("L" if i == 0 else "D"):
                n.ud(pp[i])
            else:
                c.ud(pp[i])

    p = p.get()
    n = n.get()
    c = c.get()
    return p, n, c, f


def calc_e(p, n, c, f):
    if p is None:
        if c is None or n is None:
            return []
        else:
            return [n - c]

    if n is None:
        if c is None:
            return []
        else:
            return [c - p]

    t = (n - p) / 2
    if c is None:
        return [t]

    return [t, c - p, n - c]


def calc(t, L):
    res = V(L[3])
    if L[0] is not None:
        res.ud(L[0] + t)

    if L[1] is not None:
        res.ud(L[1] - t)

    if L[2] is not None:
        res.ud(L[2])

    return res.get()


def main():
    N = int(input())
    D = {
        "R": [],
        "L": [],
        "U": [],
        "D": [],
    }

    for _ in range(N):
        x, y, d = input().split()
        x = int(x)
        y = int(y)
        D[d].append((x, y))

    VV = []
    VV.append(calc_v(D, max, 0))
    VV.append(calc_v(D, min, 0))
    VV.append(calc_v(D, max, 1))
    VV.append(calc_v(D, min, 1))

    E = {0}
    for e in [calc_e(*v) for v in VV]:
        for t in e:
            E.add(t)

    res = V(min)
    for t in E:
        if t < 0:
            continue
        res.ud((calc(t, VV[0]) - calc(t, VV[1])) * (calc(t, VV[2]) - calc(t, VV[3])))
    print(res)


def __starting_point():
    main()

__starting_point()
