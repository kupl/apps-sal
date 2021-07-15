import os, sys, re, math

N = int(input())
S = []
for i in range(N):
    S.append(input())

d = {}
for s in S:
    if not s in d:
        d[s] = 0
    d[s] += 1

d = sorted(list(d.items()), key=lambda x:x[1], reverse=True)
names = [v[0] for v in d if v[1] == d[0][1]]

for name in sorted(names):
    print(name)

