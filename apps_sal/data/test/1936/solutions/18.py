import sys
import math
input = sys.stdin.readline


def inp():
    return(int(input()))


def inara():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(list(map(int, input().split())))


t = inp()

for _ in range(t):
    l, r = invr()

    if l * 2 > r:
        print(-1, -1)
    else:
        print(l, 2 * l)
