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


n, k, q = invr()

ara = [k] * n

for i in range(q):
    x = inp()
    x -= 1
    ara[x] += 1

for i in range(n):
    if ara[i] - q > 0:
        print("Yes")
    else:
        print("No")
