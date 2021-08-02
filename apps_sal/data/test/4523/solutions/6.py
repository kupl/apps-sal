# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 05/08/2020

from sys import stdin, stdout, setrecursionlimit
from math import gcd, ceil, sqrt
from collections import Counter
from bisect import bisect_left, bisect_right
ii1 = lambda: int(stdin.readline().strip())
is1 = lambda: stdin.readline().strip()
iia = lambda: list(map(int, stdin.readline().strip().split()))
isa = lambda: stdin.readline().strip().split()
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
