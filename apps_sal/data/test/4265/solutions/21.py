"""
Created on Fri Sep 18 19:19:52 2020

@author: ezwry
"""
s = list(input())
t = list(input())
u = len(s)
ans = 0
for i in range(u):
    if s[i] != t[i]:
        ans += 1
print(ans)
