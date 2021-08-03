import sys

# import math
# from collections import deque

# import heapq

# from math import inf
# from math import gcd

# print(help(deque))
# 26


def pprint(s): return print(' '.join(map(lambda x: str(x), s)))
def input(): return sys.stdin.readline().strip()


ipnut = input
mod = 1000000007
for i in range(int(input())):
    # n, k = map(int, input().split())
    n = int(input())
    p = list(map(int, input().split()))
    pprint(reversed(p))
# c = list(map(lambda x: int(x)-1, input().split()))
