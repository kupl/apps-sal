# coding: utf-8
# Your code here!

from itertools import accumulate
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

#n,x = [int(i) for i in readline().split()]
#h,w = [int(i) for i in readline().split()]
n = int(input())
a = [int(i) for i in readline().split()]

acc = list(accumulate([0] + a))

j = 1
k = 3
ans = 10**18
for i in range(2, n):
    c = acc[i] // 2
    while j < i - 1 and acc[j] < c:
        j += 1

    c = (acc[-1] - acc[i]) // 2
    while k < n - 1 and acc[k] - acc[i] < c:
        k += 1

    for jj in range(2):
        for kk in range(2):
            l = (acc[j - jj], acc[i] - acc[j - jj], acc[-1] - acc[k - kk], acc[k - kk] - acc[i])
            res = max(l) - min(l)
            ans = min(ans, res)


print(ans)
