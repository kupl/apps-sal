import sys
# import math
# from collections import deque
# import heapq
# from math import inf
# from math import gcd

# print(help(deque))
# 26


def pprint(s): return print(' '.join(map(str, s)))
def input(): return sys.stdin.readline().strip()


ipnut = input
for i in range(int(input())):
    # n = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    print(1 + (x1 - x2) * (y1 - y2))
    # a = list(map(int,input().split()))
    # s = list(input())
