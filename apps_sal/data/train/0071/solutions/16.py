
import math
import collections
from sys import stdin, stdout, setrecursionlimit
from bisect import bisect_left as bsl
from bisect import bisect_right as bsr
import heapq as hq
setrecursionlimit(2**20)

t = 1
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().rstrip().split()))

    ans = 0
    s = 0
    for i in range(n):
        s += a[i]
        if(s < 0 and abs(s) > ans):
            ans = abs(s)

    print(ans)
