import sys
from collections import Counter
sys.setrecursionlimit(10 ** 6)
(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = x
a.sort()
i = 0
while i < len(a) and a[i] <= x:
    if a[i] == x:
        b = b + 1
    else:
        b = b - 1
    i = i + 1
print(b)
