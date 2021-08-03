#coding: utf-8
from collections import deque
from bisect import bisect_right
from math import gcd
N = int(input())
A = list(set(map(int, input().split())))
A.sort()
ans = A[0]
for a in A[1:]:
    ans = gcd(ans, a)
print(ans)
