import functools
import math
import sys

n = int(input())
a = list(map(int, input().split()))
ans = 0
a.sort()
while len(a) > 1:
    t = []
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            ans += 1
        else:
            t.append(a[i])
            #temp += 1
    a = t
print(ans)
