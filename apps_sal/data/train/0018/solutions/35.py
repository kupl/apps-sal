import sys
import math
# from collections import deque
# import heapq
# from math import inf
# from math import gcd

# print(help(deque))
# 26
pprint = lambda s: print(' '.join(map(str, s)))
input = lambda: sys.stdin.readline().strip()
ipnut = input
# a, b, c, d = map(int, input().split())
# n = int(input())
# e = list(map(int,input().split()))
for i in range(int(input())):
    n = int(input())
    print(1/math.tan(math.pi/(2*n)))
"""
10
10 11 12 13 14 15 16 17 11 11
"""

