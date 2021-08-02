from math import *

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
for i in range(n):
    if 2 * a[i] < b[i] or b[i] == 1:
        res -= 1
    else: res += b[i] // 2 * (b[i] - (b[i] // 2))
print(res)
