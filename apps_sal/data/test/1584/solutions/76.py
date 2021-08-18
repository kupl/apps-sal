"""
Created on Wed Sep  9 20:56:06 2020

@author: liang
"""

N = int(input())
L = [int(x) for x in input().split()]

L.sort()
ans = 0
for i in range(N - 2):
    p = i + 2
    for j in range(i + 1, N - 1):
        while p < N and L[p] < L[i] + L[j]:
            p += 1
        ans += max(0, p - j - 1)
print(ans)
