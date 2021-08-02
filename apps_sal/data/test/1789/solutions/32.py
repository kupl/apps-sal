import sys
import heapq as hq
import itertools
import math
import collections
ma = lambda: map(int, input().split())
lma = lambda: list(map(int, input().split()))
tma = lambda: tuple(map(int, input().split()))
ni = lambda: int(input())
yn = lambda fl: print("Yes") if fl else print("No")
ips = lambda: input().split()
ceil = math.ceil
gcd = math.gcd
RL = sys.stdin.readline
INF = 10**15


def ceilab(a, b):
    return (a + b - 1) // b


a, b, x, y = ma()
if y > 2 * x: y = 2 * x
if a == b:
    print(x)
elif a > b:
    print((a - b - 1) * y + x)
else:
    print((b - a) * y + x)
