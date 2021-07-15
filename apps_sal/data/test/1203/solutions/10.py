import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
from bisect import bisect_left

a, b = getList()
ans = (b**2 - a**2) / (2*a)

print(ans)
