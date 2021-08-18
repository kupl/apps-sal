

import math
from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
mx = 0
for i in range(n):
    print(arr[i] + mx, end=' ')
    mx = max(mx, arr[i] + mx)
print()
