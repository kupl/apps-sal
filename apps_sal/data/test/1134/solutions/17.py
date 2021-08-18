
import sys
import math


n = int(input())
arr = [int(i) for i in input().split()]
tt = [0] * n
for i in range(n):
    if(i != 0):
        tt[i] = max(tt[i - 1], arr[i] + 1)
    else:
        tt[i] = arr[i] + 1
ss = 0

for i in range(n - 1, -1, -1):
    if(i != n - 1):
        tt[i] = max(tt[i + 1] - 1, tt[i])
        ss += (tt[i] - arr[i] - 1)
    else:
        ss += (tt[i] - arr[i] - 1)
print(ss)
