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


ceil = math.ceil
gcd = math.gcd
RL = sys.stdin.readline
INF = 10**15


def ceilab(a, b):
    return (a + b - 1) // b


n = ni()
l = 0
r = n + 1
while r - l > 1:
    x = (r + l) // 2
    if x * (x + 1) // 2 > n + 1:
        r = x
    else:
        l = x
print(n + 1 - l)
