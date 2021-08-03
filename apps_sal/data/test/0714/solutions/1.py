import sys
import math
n = int(input())
z = list(map(int, input().split()))
for i in range(n):
    z[i] = [z[i], i + 1]
z.sort()
for i in range(n // 2):
    print(z[i][1], z[n - 1 - i][1])
