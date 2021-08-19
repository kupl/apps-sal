"""
Created on Fri Sep 11 01:27:46 2020

@author: liang
"""
(N, M) = map(int, input().split())
L = list()
R = list()
for i in range(M):
    (l, r) = map(int, input().split())
    L.append(l)
    R.append(r)
ans = min(R) - max(L) + 1
if ans < 0:
    ans = 0
print(ans)
