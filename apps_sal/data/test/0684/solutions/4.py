import sys
import heapq
import math


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def rinput():
    return map(int, input().split())


def rlinput():
    return list(map(int, input().split()))


def YES(flag):
    if flag:
        return "YES"
    return "NO"


def main():
    #n = int(sys.stdin.readline().strip())
    # n = iinput()
    # n, k = rinput()
    # n, m, k = rinput()
    q = rlinput()
    print(q[1], q[2], q[2])


for i in range(iinput()):
    main()
