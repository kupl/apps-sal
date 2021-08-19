"""
Created on Sun Sep 13 03:08:56 2020

@author: liang
"""
(N, K) = list(map(int, input().split()))
h = [int(input()) for _ in range(N)]
ans = 10 ** 10
h.sort()
for i in range(0, N - K + 1):
    tmp = h[i + K - 1] - h[i]
    ans = min(ans, tmp)
print(ans)
