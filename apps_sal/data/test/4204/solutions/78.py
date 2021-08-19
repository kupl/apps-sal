"""
Created on Wed Sep 16 01:17:00 2020

@author: liang
"""
S = input()
K = int(input())
for i in range(len(S)):
    if S[i] != '1':
        break
if K < i + 1:
    print(1)
else:
    print(S[i])
