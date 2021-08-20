"""
Created on Wed Sep 23 15:39:14 2020

@author: liang
"""
N = int(input())
A = [int(x) for x in input().split()]
d = [0] * N
ans = 0
for a in A:
    if a > N:
        ans += 1
    else:
        d[a - 1] += 1
for i in range(N):
    if d[i] > 0:
        if d[i] > i + 1:
            ans += d[i] - (i + 1)
        if d[i] < i + 1:
            ans += d[i]
print(ans)
