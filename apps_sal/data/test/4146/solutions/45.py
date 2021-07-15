# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:29:30 2020

@author: liang
"""

n = int(input())
E = list()
O = list()
i = 0
for v in input().split():
    if i%2 == 0:
        E.append(int(v))
    else:
        O.append(int(v))
    i += 1
#print(E)
#print(O)
edic = {-1:0}
odic = {-1:0}
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

etup = list()
otup = list()
for e in edic.keys():
    etup.append((e,edic[e]))
for o in odic.keys():
    otup.append((o,odic[o]))    
etup.sort(reverse=True,key=lambda x:x[1])
otup.sort(reverse=True,key=lambda x:x[1])

#print(etup)
#print(otup)
i = 0
j = 0
while True:
    ekey, etmp = etup[i]
    okey, otmp = otup[j]
    if ekey != okey:
        break
    if etup[i+1][1] < otup[j+1][1]:
        j += 1
    else:
        i += 1
    #rint("calc")

#print(edic)

ans = n - etmp - otmp
    
print(ans)
