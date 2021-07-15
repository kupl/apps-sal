#!/usr/bin/env python3
import sys

#lines = stdin.readlines()
def rint():
    return list(map(int, sys.stdin.readline().split()))

def input():
    return sys.stdin.readline().rstrip('\n')

def oint():
    return int(input())


q = oint()

for _ in range(q):
    n, r = rint()
    x = set(rint())
    x = list(x)
    x.sort()
    z = 0
    si = 0
    n = len(x)
    ei = n-1
    cnt = 0
    while True:
        if ei < si:
            break
        cnt += 1
        ei -=1
        z +=r
        for i in range(si, ei+1):
            if x[i] > z:
                si = i
                break
            if i == ei:
                si = ei+1
    print(cnt)




