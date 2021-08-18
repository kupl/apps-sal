"""
Created on Tue Sep  8 01:07:55 2020

@author: liang
"""

N, K = map(int, input().split())
H = [int(x) for x in input().split()]
H.sort()

if N > K:
    ans = sum(H[:N - K])
else:
    ans = 0
print(ans)
