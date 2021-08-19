from math import sqrt, factorial, gcd, log2, inf, ceil
import heapq
from collections import defaultdict
from bisect import bisect_left
from bisect import bisect_right
import sys
from sys import stdin
from collections import deque
mod = 10 ** 9 + 7
n = int(input())
l = list(map(int, input().split()))
la = [i + 1 for i in range(n)]
s = set(la)
yo = set()
for i in l:
    if i is not 0:
        s.remove(i)
        yo.add(i)
k = list(s)
k.sort()
for i in range(n):
    if l[i] == 0:
        z = k.pop()
        l[i] = z
for i in range(n):
    if l[i] == i + 1:
        for j in range(n):
            if l[j] not in yo:
                if l[j] == j + 1 and i != j:
                    (l[i], l[j]) = (l[j], l[i])
                    break
                elif l[j] != i + 1 and l[i] != j + 1:
                    (l[i], l[j]) = (l[j], l[i])
                    break
        break
print(*l)
