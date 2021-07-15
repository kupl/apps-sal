import sys
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
import math,itertools

"""
"""

def solve():
    N, X = getInts()
    if N <= 2:
        return 1
    N -= 3
    return N//X + 2
    
#print(solve())
for _ in range(getInt()):
    print(solve())
    

