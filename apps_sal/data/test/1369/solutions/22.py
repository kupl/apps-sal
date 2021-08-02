# coding: utf-8

import math

N = int(input())

xy = []
for i in range(N):
    xy.append([int(p) for p in input().split()])


def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def max_dist(a):
    max_d = 0
    for b in xy:
        max_d = max(max_d, dist(a, b))
    return max_d


def g(a):
    ly = 0
    ry = 1000
    for j in range(100):
        #print("    ly = " + str(ly) + " ry = " + str(ry))
        c1 = (ly * 2 + ry) / 3
        c2 = (ly + ry * 2) / 3
        if max_dist([a, c1]) > max_dist([a, c2]):
            ly = c1
        else:
            ry = c2
    return max_dist([a, ly])


lx = 0
rx = 1000
for i in range(100):
    #print("lx = " + str(lx) + " rx = " + str(rx))
    c1 = (lx * 2 + rx) / 3
    c2 = (lx + rx * 2) / 3
    if g(c1) > g(c2):
        lx = c1
    else:
        rx = c2

print(g(lx))
