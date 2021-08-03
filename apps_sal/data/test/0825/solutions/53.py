import math
import numpy as np
n = int(input())

s = math.sqrt(n)
i = 2
f = {}
while i <= s:
    while n % i == 0:
        f[i] = f.get(i, 0) + 1
        n = n // i
    i += 1

ans = 0
for x in f.values():
    e = 0
    cumsum = 0
    while e + cumsum + 1 <= x:
        e += 1
        cumsum += e
    ans += e
print(ans + (n > 1))
