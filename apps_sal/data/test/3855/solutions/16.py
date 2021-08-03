from math import log2
n = int(input())

a = log2(n + 1)
res = int(a)
if a - res > 0:
    res += 1

print(res)
