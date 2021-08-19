#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
sp = [[]for i in range(n)]
ns = []
for i in range(2 * n - 2):
    s = input()
    sp[len(s)].append(s)
    ns.append(s)
s1 = sp[n - 1][0] + sp[n - 1][1][-1]
s2 = sp[n - 1][1][0] + sp[n - 1][0]

ss = [s1, s2]
correct_s = ''
res = True
ii = 0
correct_s = ss[ii]
for i in range(1, n):
    if correct_s[:i] == sp[i][0] and correct_s[-i:] == sp[i][1]:
        continue
    if correct_s[:i] == sp[i][1] and correct_s[-i:] == sp[i][0]:
        continue
    res = False
    break
if res:
    pass
else:
    correct_s = ss[1]
ans = ''
f = [0] * n
for s in ns:
    if f[len(s)] == 0:
        if correct_s[:len(s)] == s:
            ans += 'P'
            f[len(s)] = 1
        else:
            ans += 'S'
            f[len(s)] = 2
    else:
        res = 'P' if f[len(s)] == 2 else 'S'
        ans += res
print(ans)
