import math
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = 10**9

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(item) for item in input().split()]
    if len(a) == 1:
        print(-1)
        continue
    seen = dict()
    ret = INF
    for i, item in enumerate(a):
        if item not in seen:
            seen[item] = i
        else:
            ret = min(ret, abs(seen[item] - i) + 1)
            seen[item] = i
    if ret == INF:
        print(-1)
    else:
        print(ret)
