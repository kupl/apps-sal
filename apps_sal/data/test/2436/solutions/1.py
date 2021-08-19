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
    n = int(input())
    # n,k = map(int,input().split())
    a = list(map(int, input().split()))
    # s = list(input())
    ans = 1
    a.sort()
    for i in range(n):
        if i + 1 >= a[i]:
            ans = i + 2
    print(ans)
