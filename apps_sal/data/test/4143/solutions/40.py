from math import *

n = int(input())
a = [int(input()) for _ in range(5)]

ans = ceil(n / a[0])
min = 0
for i in range(1, 5):
    if a[i] >= a[min]:
        ans += 1
    else:
        ans = ceil(n / a[i]) + i
        min = i

print(ans)
