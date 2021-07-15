import math
import collections
import sys


def inpu():
    return input().split(' ')


def inti(a):
    for i in range(len(a)):
        a[i] = int(a[i])
    return a


def inp():
    a = inpu()
    a = inti(a)
    return a


for _ in range(int(input())):
    n = int(input())
    moves = 0
    if n % 6 == 0:
        while n % 6 == 0:
            n = n//6
            moves += 1
    if n % 3 == 0:
        while n % 3 == 0:
            n = n//3
            moves += 2
    if n == 1:
        print(moves)
    else:
        print(-1)

