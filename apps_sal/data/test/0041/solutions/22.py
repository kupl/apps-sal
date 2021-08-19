import sys
import math
n = int(input())
a = list(map(int, input().split()))
ans = [n for i in range(n)]
lind = -n
for i in range(n):
    if a[i] == 0:
        lind = i
    ans[i] = min(ans[i], abs(i - lind))
lind = -n
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        lind = i
    ans[i] = min(ans[i], abs(i - lind))
for i in range(n):
    print(ans[i], end=' ')
