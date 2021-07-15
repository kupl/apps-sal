#!/usr/bin/env python3
from sys import stdin


def solve(tc):
    n, k = map(int, stdin.readline().split())

    for i in range(k):
        if n%10==0:
            n //= 10
        else:
            n -= 1
    
    print(n)
    # items = map(int,stdin.readline().split())
    pass


LOCAL_TEST = not __debug__
if LOCAL_TEST:
    infile = __file__.split('.')[0] + "-test.in"
    stdin = open(infile, 'r')

tcs = (int(stdin.readline().strip()) if LOCAL_TEST else 1)
tc = 1
while tc <= tcs:
    solve(tc)
    tc += 1
