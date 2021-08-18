import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


def main():
    n = getN()
    if n % 4 == 1:
        print("0 A")
    elif n % 4 == 3:
        print("2 A")
    elif n % 4 == 2:
        print("1 B")
    else:
        print("1 A")


def __starting_point():
    main()


__starting_point()
