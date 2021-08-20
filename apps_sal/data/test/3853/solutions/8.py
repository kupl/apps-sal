from math import *
n = int(input())
mx = 0
for i in range(n):
    (k, a) = list(map(int, input().split()))
    mx = max(mx, 2 * k + log2(a))
    mx = max(mx, 2 * (k + 1))
print(int(ceil(mx / 2)))
