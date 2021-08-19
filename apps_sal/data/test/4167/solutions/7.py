"""
Created on Mon Oct  5 21:22:55 2020

@author: liang
"""
(N, K) = map(int, input().split())
if K % 2 == 0:
    ans = (N // K) ** 3 + ((N + K // 2) // K) ** 3
    print(ans)
else:
    print((N // K) ** 3)
