import sys
from collections import defaultdict
t = 1
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, sys.stdin.readline().strip().split()))
    op = 0
    for j in range(1, n):
        if a[j] > a[j - 1]:
            continue
        else:
            op += a[j - 1] - a[j]
    print(op)
