"""
    Template written to be used by Python Programmers.
    Use at your own risk!!!!
    Owned by adi0311(rating - 5 star at CodeChef and Specialist at Codeforces).
"""
import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush, nlargest, nsmallest, _heapify_max, _heapreplace_max
from math import ceil, floor, gcd, fabs, factorial, fmod, sqrt, inf, log
from collections import defaultdict as dd, deque, Counter as c
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from fractions import Fraction
# sys.setrecursionlimit(2*pow(10, 6))
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")
mod = pow(10, 9) + 7
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(var): sys.stdout.write(str(var))
def outln(var): sys.stdout.write(str(var)+"\n")
def l(): return list(sp())
def sl(): return list(ssp())
def sp(): return list(map(int, data().split()))
def ssp(): return list(map(str, data().split()))
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


temp = pow(10, 8)


def dfs(number):
    if 0 < number <= n:
        answer[0] += 1
    if number >= temp:
        return
    for i in range(10):
        if number * 10 + i > 0:
            if len(set(str(number * 10 + i))) <= 2:
                dfs(number * 10 + i)


n = int(data())
answer = [0]
dfs(0)
if n == pow(10, 9):
    outln(answer[0] + 1)
    return
outln(answer[0])

