'''
    Author : thekushalghosh
    Team   : CodeDiggers
'''
import sys,math
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
i = 1
while i > 0:
    q = a[-i] - a[i - 1]
    if (a[i] - a[i - 1]) * i >= k:
        q = q - (k // i)
        break
    k = k + (a[i - 1] * i) - (a[i] * i)
    q = a[-i] - a[i]
    if (a[-i] - a[-i - 1]) * i >= k:
        q = q - (k // i)
        break
    k = k + (a[-i - 1] * i) - (a[-i] * i)
    i = i + 1
    if not q:
        break
print(q)
