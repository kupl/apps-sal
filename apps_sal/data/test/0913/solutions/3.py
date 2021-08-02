import math
import collections
import sys
input = sys.stdin.readline
n = int(input())
r = list(map(int, input().split()))
b = list(map(int, input().split()))
countr, countb = 0, 0
for i in range(n):
    if r[i] and not b[i]:
        countr += 1
    elif not r[i] and b[i]:
        countb += 1
if countr == 0:
    print(-1)
    return
print(countb // countr + 1)
