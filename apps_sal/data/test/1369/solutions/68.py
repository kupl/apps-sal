from collections import deque, defaultdict, Counter
from math import sqrt
import numpy as np
from functools import reduce
import heapq
import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys


def I():
    return int(sys.stdin.readline().rstrip())


def MI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


class Vector:

    def __init__(self, ls):
        """
        ls ... list
        """
        self.vec = ls

    def __len__(self):
        return len(self.vec)

    def __getitem__(self, idx):
        return self.vec[idx]

    def __repr__(self):
        return f'Vector({self.vec})'

    def add(self, vec):
        """
        vec ... vector class
        """
        assert len(self) == len(vec)
        ret = [a + b for (a, b) in zip(self.vec, vec.vec)]
        return Vector(ret)

    def sub(self, vec):
        """
        vec ... vector class
        """
        assert len(self) == len(vec)
        ret = [a - b for (a, b) in zip(self.vec, vec.vec)]
        return Vector(ret)

    def mul(self, vec):
        """
        vec ... vector class
        """
        assert len(self) == len(vec)
        ret = [a * b for (a, b) in zip(self.vec, vec.vec)]
        return Vector(ret)

    def norm(self):
        tmp = sum([x * x for x in self.vec])
        return sqrt(tmp)


def norm(vec):
    """
    vec ... Vector class
    """
    return vec.norm()


def cross(a, b):
    """
    Outer product for 2d
    a,b ... Vector class
    """
    assert len(a) == 2 and len(b) == 2
    first = a[0] * b[1]
    second = a[1] * b[0]
    return first - second


def dot(a, b):
    return sum(a.mul(b))


EPS = 1e-10


def is_ccw(p0, p1, p2):
    """
    p1-p0に対してp2-p0が`基本的に`反時計回りならばTrueを返す。
    同一直線上にあってもconvex hulをつくるのには含めて良いので、popする必要はない、したがってFalseをァ得すことにする
    """
    a = p1.sub(p0)
    b = p2.sub(p0)
    if cross(a, b) > EPS:
        return True
    else:
        return False


def convex_hull(points: list):
    points.sort(key=lambda x: (x[0], x[1]))
    if len(points) < 3:
        pass
    conv_upper = [points[0], points[1]]
    for p in points[2:]:
        while len(conv_upper) >= 2 and is_ccw(conv_upper[-2], conv_upper[-1], p):
            conv_upper.pop()
        conv_upper.append(p)
    points = points[::-1]
    conv_lower = [points[0], points[1]]
    for p in points[2:]:
        while len(conv_lower) >= 2 and is_ccw(conv_lower[-2], conv_lower[-1], p):
            conv_lower.pop()
        conv_lower.append(p)
    ret = conv_upper[1:-1] + conv_lower
    return ret[::-1]


def main():
    N = I()
    points = []
    for i in range(N):
        points.append(Vector(list(MI())))
    ans = convex_hull(points)
    X = len(ans)
    dist_list = []
    for i in range(X):
        for j in range(X):
            dist = pow((ans[i][0] - ans[j][0]) ** 2 + (ans[i][1] - ans[j][1]) ** 2, 0.5)
            dist_list.append((dist, i, j))
    dist_list.sort(key=lambda tup: tup[0], reverse=True)
    x_ = (ans[dist_list[0][1]][0] + ans[dist_list[0][2]][0]) / 2
    y_ = (ans[dist_list[0][1]][1] + ans[dist_list[0][2]][1]) / 2
    max_dist = dist_list[0][0] / 2
    cnt = 0
    for a in ans:
        ran = pow((a[0] - x_) ** 2 + (a[1] - y_) ** 2, 0.5)
        if ran > max_dist:
            break
        cnt += 1
    if cnt == X:
        print(max_dist)
        return
    dif_list = []
    for i in range(X):
        for j in range(X):
            for k in range(X):
                if i == j or j == k or i == k:
                    continue
                ra = np.array([ans[i][0], ans[i][1]])
                rb = np.array([ans[j][0], ans[j][1]])
                rc = np.array([ans[k][0], ans[k][1]])
                A = np.dot(rb - rc, rb - rc)
                B = np.dot(rc - ra, rc - ra)
                C = np.dot(ra - rb, ra - rb)
                T = A * (B + C - A)
                U = B * (C + A - B)
                W = C * (A + B - C)
                rcc = (T * ra + U * rb + W * rc) / (T + U + W)
                px = rcc[0]
                py = rcc[1]
                dif = pow((px - ans[i][0]) ** 2 + (py - ans[i][1]) ** 2, 0.5)
                cnt_ = 0
                for a in ans:
                    ran = pow((a[0] - px) ** 2 + (a[1] - py) ** 2, 0.5)
                    if ran > dif:
                        break
                    cnt_ += 1
                if cnt_ == X:
                    dif_list.append(dif)
    print(min(dif_list))


def __starting_point():
    main()


__starting_point()
