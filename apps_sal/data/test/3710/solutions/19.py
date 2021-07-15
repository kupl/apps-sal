import sys, math
input = sys.stdin.readline

def getInts():
    return [int(s) for s in input().split()]

def getInt():
    return int(input())

def getStrs():
    return [s for s in input().split()]

def getStr():
    return input().strip()

def listStr():
    return list(input().strip())

import collections as col
import math

def solve():
    #we need to know whether, amongst the C values, there are two or more pairwise coprime values whose product equals K
    N, K = getInts()
    C = getInts()
    lcm = 1
    for c in C:
        lcm = lcm*c//math.gcd(lcm,c)
        lcm = math.gcd(lcm,K)
    return "Yes" if lcm == K else "No"
    
#for _ in range(getInt()):
print(solve())
    


