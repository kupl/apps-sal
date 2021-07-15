#!/usr/bin/env python3
from sys import stdin, stdout

def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


t = int(input())

for i in range(t):
    n, k = rint()
    x = []
    x = list(rint())
    ans = 0
    ans = max(ans, x[0])
    ans = max(ans, n-x[-1]+1)

    if k < 1:
        print(ans)
        continue

    for ii in range(0, k-1):
        ans = max(ans, (x[ii+1]-x[ii])//2+1)
    print(ans)



