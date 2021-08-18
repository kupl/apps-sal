"""
Created on Sun Sep 27 03:05:21 2020

@author: liang
"""

N, T = map(int, input().split())

time = [int(x) for x in input().split()]

ans = 0
for i in range(N - 1):
    ans += min(T, time[i + 1] - time[i])
ans += T
print(ans)
