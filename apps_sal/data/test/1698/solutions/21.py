import math
import sys
import os

n, k = map(int, input().split())

step = list(map(int, input().split()))


step.sort()
step.reverse()


if n > k:
    z = int(round(n / k + 0.5))
    res = 0
    for i in range(z):
        if k < len(step):
            res += 2 * (step[0] - 1)
            del step[:k]
        else:
            res += 2 * (step[0] - 1)
else:
    res = 2 * (step[0] - 1)
print(res)
