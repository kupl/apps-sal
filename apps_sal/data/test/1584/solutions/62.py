"""
Created on Wed Sep  9 21:39:55 2020

@author: liang
"""

"""
Created on Wed Sep  9 20:56:06 2020

@author: liang
"""

from bisect import bisect_left
N = int(input())
L = [int(x) for x in input().split()]


L.sort()
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        t = L[i] + L[j]
        p = bisect_left(L, t)
        ans += max(0, p - j - 1)
print(ans)
