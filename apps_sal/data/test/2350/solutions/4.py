import sys
import heapq


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def rinput():
    return map(int, input().split())


def rlinput():
    return list(map(int, input().split()))


def srlinput():
    return sorted(list(map(int, input().split())))


def main():
    #n = int(sys.stdin.readline().strip())
    #n = iinput()
    #n, k = rinput()
    #n, m = rinput()
    #n, m, k = rinput()
    #n, k, m = rinput()
    #q = srlinput()
    #s = input()

    x, y, x1, y1 = rinput()
    print(1 + (x - x1) * (y - y1))


for i in range(iinput()):
    main()
