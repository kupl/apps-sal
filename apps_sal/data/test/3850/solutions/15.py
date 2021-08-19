from collections import deque, defaultdict
import random
import math as mt
import sys
import string
input = sys.stdin.readline
# print=sys.stdout.write
def L(): return list(map(int, input().split()))
def Ls(): return list(input().split())


def M(): return list(map(int, input().split()))
def I(): return int(input())


n, k, p = M()
l = L()
g = L()
l.sort()
g.sort()
ans = 10**30
for i in range(k - n + 1):
    ans1 = 0
    for j in range(i, i + n):
        ans1 = max(ans1, abs(l[j - i] - g[j]) + abs(g[j] - p))
    ans = min(ans, ans1)
print(ans)
