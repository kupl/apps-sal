"""
Created on Thu Sep 10 11:33:13 2020

@author: liang
"""
(L, R) = map(int, input().split())
r = R % 2019
l = L % 2019
ans = 2018
if R - L >= 2019 - l or l == 0:
    ans = 0
else:
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            ans = min(ans, i * j % 2019)
print(ans)
