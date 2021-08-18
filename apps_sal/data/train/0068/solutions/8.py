import sys
import math
import io
import os
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write('\n'.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


INF = float('inf')
mod = 10**9 + 7


for t in range(int(data())):
    n = int(data())
    s = data()
    ind = 0
    l = []
    for i in range(1, n):
        if s[i] != s[i - 1]:
            l.append(i - ind)
            ind = i
    l.append(n - ind)
    l = l[::-1]
    i = 0
    ans = 0
    j = len(l) - 1
    while l:
        if l[-1] > 1:
            ans += 1
            l.pop()
            j -= 1
        else:
            j = min(j, len(l) - 1)
            while j >= 0 and l[j] == 1:
                j -= 1
            if j == -1:
                l.pop()
                if l:
                    l.pop()
            else:
                l.pop()
                l[j] -= 1
            ans += 1
    out(ans)
