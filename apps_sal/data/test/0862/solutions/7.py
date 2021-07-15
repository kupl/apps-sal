#!/usr/bin/env python3
from sys import stdin


def solve(tc):
    n = int(stdin.readline().strip())
    li = list(map(int,stdin.readline().split()))

    ans = 1
    mini = 1e9
    for i in range(n):
        k = li[i] // n
        if li[i]%n>i:
            k += 1
        
        if k<mini:
            mini = k
            ans = i+1
    
    print(ans)



LOCAL_TEST = not __debug__
if LOCAL_TEST:
    infile = __file__.split('.')[0] + "-test.in"
    stdin = open(infile, 'r')

tcs = (int(stdin.readline().strip()) if LOCAL_TEST else 1)
tc = 1
while tc <= tcs:
    solve(tc)
    tc += 1
