"""
Created on Fri Sep 11 01:37:10 2020

@author: liang
"""

S = input()
N = len(S)
ans = 0
for i in range(N):
    if i % 2 == 0 and S[i] == "0":
        ans += 1
    if i % 2 == 1 and S[i] == "1":
        ans += 1
ans = min(ans, N - ans)
print(ans)
