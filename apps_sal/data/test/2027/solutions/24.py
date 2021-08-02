import sys
import math
n = int(input())
z = list(map(int, input().split()))
z.append(0)
for i in range(n):
    print(z[i] + z[i + 1], end=' ')
