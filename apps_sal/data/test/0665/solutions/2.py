import sys
from collections import Counter
from math import *
for _ in range(int(input())):
    (n, s) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if sum(a) <= s:
        print(0)
        continue
    L = 0
    R = n + 1
    ans = 0
    while R - L > 1:
        m = (L + R) // 2
        if sum(a[:m]) - max(a[:m]) > s:
            R = m
        else:
            L = m
            ans = a.index(max(a[:m]))
    print(ans + 1)
