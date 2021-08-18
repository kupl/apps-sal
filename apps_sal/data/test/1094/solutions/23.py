"""
Created on Sun Mar 13 19:40:03 2016

@author: Kostya S.
"""

n = int(input())
d = {}
p = 1
for _ in range(n):
    s = input()
    d[s] = p
    p += 1
t = []
for k, v in d.items():
    t.append((v, k))
t = sorted(t, reverse=True)

for e in t:
    print(e[1])
