from math import sqrt, ceil, floor
from sys import stdin, stdout
from heapq import heapify, heappush, heappop
import string
import bisect


n, t = list(map(int, stdin.readline().split()))
ans = 1
ans_t = 9999999
for i in range(n):
    s, d = list(map(int, stdin.readline().split()))
    if s < t:
        s = s + ceil((t - s) / d) * d
    if ans_t > s:
        ans = i + 1
        ans_t = s
print(ans)
