__author__ = 'Michael Ilyin'

import math

debug = False


def dist(x1, y1, x2, y2):
    return math.sqrt(math.pow(math.fabs(x1 - x2), 2) + math.pow(math.fabs(y1 - y2), 2))


def get_y(x1, y1, x2, y2, x):
    return (((x - x1) * (y2 - y1)) / (x2 - x1)) + y1


if debug:
    with open("input.txt", "r") as inp:
        firstLine = inp.readline()
        secondLine = inp.readline()
        thirdLine = inp.readline()
        fourthLine = inp.readline()
else:
    firstLine = input()
    secondLine = input()
    thirdLine = input()
    fourthLine = input()

first = firstLine.split()
n = float(first[0])
m = float(first[1])
a = float(first[2])
b = float(first[3])

A = [float(x) for x in secondLine.split()]
B = [float(x) for x in thirdLine.split()]
L = [float(x) for x in fourthLine.split()]

if debug:
    print(A)
    print(B)
    print(L)

optimalLen = float("inf")
optimalBIdx = -1
for i, bi in enumerate(B):
    d = dist(0, 0, b, bi) + L[i]
    if d <= optimalLen:
        optimalLen = d
        optimalBIdx = i

if debug:
    print(optimalBIdx + 1, optimalLen)

intersectY = get_y(0, 0, b, B[optimalBIdx], a)

if debug:
    print(intersectY)

pointDist = float("inf")
optimalAIdx = -1
for i, ai in enumerate(A):
    d = dist(a, ai, a, intersectY)
    if d < pointDist:
        pointDist = d
        optimalAIdx = i

if debug:
    print(optimalAIdx + 1, pointDist)

optimalLen = float("inf")
optimalBIdx = -1
for i, bi in enumerate(B):
    d = dist(a, A[optimalAIdx], b, bi) + L[i]
    if d <= optimalLen:
        optimalLen = d
        optimalBIdx = i

print(optimalAIdx + 1, optimalBIdx + 1)
