# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 22:36:36 2020

@author: liang
"""

N, K = list(map(int, input().split()))
R, S, P = list(map(int, input().split()))
T = input()
hand = {"r": P, "s": R, "p": S}
ans = 0
for i in range(K):
    s = str()
    tmp = i
    while tmp < N:
        s += T[tmp]
        tmp += K
    # print(s)
    count = 1
    prev = str()
    for j in range(len(s)):
        if s[j] == prev:
            count += 1
        else:
            count = 1
        if count % 2 == 0:
            continue
        prev = s[j]
        """
        if s[j] == "r":
            ans += P
        elif s[j] == "s":
            ans += R
        else:
            ans += S
        """
        ans += hand[s[j]]
print(ans)
