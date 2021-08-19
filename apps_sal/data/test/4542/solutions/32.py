"""
Created on Wed Sep 30 02:12:31 2020

@author: liang
"""
S = input()
ans = 0
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        ans += 1
print(ans)
