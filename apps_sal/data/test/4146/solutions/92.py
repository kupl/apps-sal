# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:11:38 2020

@author: liang
"""

"""
【２番目の取得】
"""
n = int(input())
E = list()
O = list()
i = 0
for v in input().split():
    if i % 2 == 0:
        E.append(int(v))
    else:
        O.append(int(v))
    i += 1
# print(E)
# print(O)
edic = {}
odic = {}
for e in E:
    if e not in edic.keys():
        edic[e] = 1
    else:
        edic[e] += 1

for o in O:
    if o not in odic.keys():
        odic[o] = 1
    else:
        odic[o] += 1

etmp = [(-1, 0), (-1, 0)]
otmp = [(-1, 0), (-1, 0)]

for key in edic.keys():
    # first
    if edic[key] > etmp[0][1]:
        etmp[1] = etmp[0]
        etmp[0] = (key, edic[key])
    # second
    elif edic[key] > etmp[1][1]:
        etmp[1] = (key, edic[key])

for key in odic.keys():
    # first
    if odic[key] > otmp[0][1]:
        otmp[1] = otmp[0]
        otmp[0] = (key, odic[key])
    # second
    elif odic[key] > otmp[1][1]:
        otmp[1] = (key, odic[key])

if etmp[0][0] == otmp[0][0]:
    ans = max(etmp[0][1] + otmp[1][1], etmp[1][1] + otmp[0][1])
else:
    ans = etmp[0][1] + otmp[0][1]
print(n - ans)
