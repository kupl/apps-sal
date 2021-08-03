import sys
# from collections import deque

# print(help(deque))
# 26


def input(): return sys.stdin.readline().strip()


ipnut = input
for i in range(int(input())):
    n, m = map(int, ipnut().split())
    if n == m == 2 or min(n, m) == 1:
        print("YES")
    else:
        print("NO")
    # n = int(input())
    # s = list(map(int,input()))
"""
10
10 11 12 13 14 15 16 17 11 11
"""
