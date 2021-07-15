import sys
import math

N = int(input())

a = list(map(int, input().split()))

a.sort()
ans = 10**9
for i in range(a[0], a[-1]+1):
    cost = 0
    for j in a:
        cost += (i-j)**2
    ans = min(cost, ans)
print(ans)
