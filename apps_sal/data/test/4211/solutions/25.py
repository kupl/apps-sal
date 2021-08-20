"""
Created on Wed Sep  9 16:47:54 2020

@author: liang
"""
INF = 10 ** 6
N = int(input())
B = [INF] + list(map(int, input().split())) + [INF]
ans = 0
for i in range(1, N + 1):
    ans += min(B[i - 1], B[i])
print(ans)
