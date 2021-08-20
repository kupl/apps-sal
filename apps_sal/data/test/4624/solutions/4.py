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
    (n, x) = list(map(int, stdin.readline().rstrip().split()))
    if n == 1 or n == 2:
        print(1)
    else:
        n -= 2
        cnt = 1
        while n > 0:
            n -= x
            cnt += 1
        print(cnt)
