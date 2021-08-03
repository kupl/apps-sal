import sys
import math
from random import randint
n, k = map(int, input().split())
y = list(map(int, input().split()))
ans = 0
for i in range(n):
    if k + y[i] <= 5:
        ans += 1
print(ans // 3)
