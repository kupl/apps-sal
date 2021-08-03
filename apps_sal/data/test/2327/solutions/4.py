# from decorators import *
from sys import stdin, stdout
from math import ceil

# @debug


def solve(n):
    c = 0
    while n > 0:
        c += n
        n //= 2

    print(c)


for _ in range(int(input())):
    n = int(stdin.readline())
    # s = list(map(int,stdin.readline().split()))
    solve(n)
