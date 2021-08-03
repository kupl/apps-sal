import sys
import random
from fractions import Fraction
from math import *


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def finput():
    return float(input())


def tinput():
    return input().split()


def linput():
    return list(input())


def rinput():
    return list(map(int, tinput()))


def fiinput():
    return list(map(float, tinput()))


def rlinput():
    return list(map(int, input().split()))


def trinput():
    return tuple(rinput())


def srlinput():
    return sorted(list(map(int, input().split())))


def NOYES(fl):
    if fl:
        print("NO")
    else:
        print("YES")


def YESNO(fl):
    if fl:
        print("YES")
    else:
        print("NO")


def main():
    n, l = rinput()
    #n = iinput()
    #k = iinput()
    #m = iinput()
    #n = int(sys.stdin.readline().strip())
    #n, k = rinput()
    #n, m = rinput()
    #m, k = rinput()
    #n, k, m = rinput()
    #n, m, k = rinput()
    #k, n, m = rinput()
    #k, m, n = rinput()
    #m, k, n = rinput()
    #m, n, k = rinput()
    q = rlinput()
    #q = linput()
    q = [0] + q + [l]
    w, e = [0] * (n + 2), [0] * (n + 2)

    for i in range(1, n + 2):
        e[n + 1 - i] = e[n + 2 - i] + ((q[-i] - q[-1 - i]) / i)
        w[i] = w[i - 1] + ((q[i] - q[i - 1]) / i)

    left, right = 0, n + 2
    while right > left + 1:
        mid = (right + left) // 2
        if w[mid] >= e[mid]:
            right = mid
        else:
            left = mid

    print((q[right] - q[right - 1] - (max(0, w[right - 1] - e[right]) * (n - right + 2) + max(0, e[right] - w[right - 1]) * right)) / (n + 2) + max(w[right - 1], e[right]))


for i in range(iinput()):
    main()
