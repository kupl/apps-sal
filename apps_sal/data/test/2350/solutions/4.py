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

    x, y, x1, y1 = rinput()
    print(1 + (x - x1) * (y - y1))


for i in range(iinput()):
    main()
