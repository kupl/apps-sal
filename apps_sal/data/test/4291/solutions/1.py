"""
Created on Mon Sep 14 00:57:13 2020

@author: liang
"""

N, Q = list(map(int, input().split()))
S = input()
S += "a"
d = [0] * (N + 1)
count = 0
for i in range(len(S) - 1):
    if S[i:i + 2] == "AC":
        count += 1
    d[i + 1] = count
for i in range(Q):
    l, r = list(map(int, input().split()))
    ans = d[r - 1] - d[l - 1]
    print(ans)
