import sys
import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("Yes") if fl else print("No")
def ips(): return input().split()


k = ni()
n = 50
p, r = divmod(k, n)
ans = [0] * n
for i in range(n):
    if i < n - r:
        ans[i] = i + p
    else:
        ans[i] = i + 1 + p
print(n)
print(*ans)
