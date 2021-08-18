import copy
import sys


def solve():
    n = int(input())
    for reg in range(n):
        temp = help()
        print(-1 if temp == 1000 else temp)


def help():
    res = 1000
    read = [list(map(int, input().split())) for _ in range(4)]
    for _1 in range(4):
        for _2 in range(4):
            for _3 in range(4):
                for _4 in range(4):
                    l = copy.deepcopy(read)
                    for i in range(_1):
                        rot(l[0])
                    for i in range(_2):
                        rot(l[1])
                    for i in range(_3):
                        rot(l[2])
                    for i in range(_4):
                        rot(l[3])
                    if square(l):
                        res = min(res, _1 + _2 + _3 + _4)
    return res


def rot(l):
    x = l[0]
    y = l[1]
    homex = l[2]
    homey = l[3]
    yabove = y - homey
    xright = x - homex
    newx = homex - yabove
    newy = homey + xright
    l[0] = newx
    l[1] = newy
    return l


def square(l):
    distances = list()
    for i in range(4):
        for j in range(i + 1, 4):
            distances.append(dist(l[i], l[j]))
    distances.sort()
    if distances[0] < 0.000001:
        return False
    different = 0
    for i in range(len(distances) - 1):
        if abs(distances[i] - distances[i + 1]) > 0.000001:
            different += 1
    return different == 1


def dist(a, b):
    return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])


if sys.hexversion == 50594544:
    sys.stdin = open("test.txt")
solve()
