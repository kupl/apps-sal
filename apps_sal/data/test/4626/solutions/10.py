import sys
import math
t = int(input())
for _ in range(t):
    (a, b, c) = list(map(int, input().split()))
    maxL = min(a, b, c)
    maxR = max(a, b, c)
    maxR -= 1
    maxL += 1
    print(max(0, (maxR - maxL) * 2))
