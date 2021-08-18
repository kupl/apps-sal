import collections
import math

n = int(input())
x = int((math.sqrt(1 + 8 * n) - 1) / 2)
t = (x + 1) * x // 2
if t == n:
    print(x)
else:
    print(n - t)
