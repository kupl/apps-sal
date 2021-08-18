
from sys import stdin, stdout, setrecursionlimit
from math import gcd, ceil, sqrt
from collections import Counter
from bisect import bisect_left, bisect_right
def ii1(): return int(stdin.readline().strip())
def is1(): return stdin.readline().strip()
def iia(): return list(map(int, stdin.readline().strip().split()))
def isa(): return stdin.readline().strip().split()


setrecursionlimit(100000)
mod = 1000000007

tc = ii1()
for _ in range(tc):
    n = ii1()
    arr = sorted(iia())
    for i in range(1, n):
        if arr[i] - arr[i - 1] > 1:
            print('NO')
            break
    else:
        print('YES')
