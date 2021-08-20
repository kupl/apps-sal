import math
import collections
from sys import stdin, stdout, setrecursionlimit
from bisect import bisect_left as bsl
from bisect import bisect_right as bsr
import heapq as hq
setrecursionlimit(2 ** 20)
t = 1
t = int(stdin.readline())
for _ in range(t):
    (n, m) = list(map(int, stdin.readline().rstrip().split()))
    chk = False
    for i in range(n):
        r1 = list(map(int, stdin.readline().rstrip().split()))
        r2 = list(map(int, stdin.readline().rstrip().split()))
        if r1[1] == r2[0]:
            chk = True
    if m % 2 == 1:
        print('NO')
        continue
    if chk:
        print('YES')
    else:
        print('NO')
