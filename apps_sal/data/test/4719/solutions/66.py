"""
Created on Tue Sep 29 14:54:30 2020

@author: liang
"""
n = int(input())
S = [input() for _ in range(n)]
ans = [100] * 26
for i in range(n):
    tmp = [0] * 26
    for s in S[i]:
        key = ord(s) - ord('a')
        if tmp[key] < ans[key]:
            tmp[key] += 1
    ans = tmp.copy()
res = ''
for i in range(26):
    res += chr(ord('a') + i) * tmp[i]
print(res)
