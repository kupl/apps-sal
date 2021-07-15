from math import *
import sys
input = lambda: sys.stdin.readline().strip()

d = {'m': [], 's': [], 'p': []}

ls = list(input().split())
for i in ls:
    d[i[1]].append(int(i[0]))
for k, v in list(d.items()):
    v.sort()
    if len(v)==3 and len(set(v))==1: print((0)); break
    if len(v)==3 and v[0]+1==v[1] and v[1]+1==v[2]: print((0)); break
else:
    for k, v in list(d.items()):
        if len(v)==2 and len(set(v))==1: print((1)); break
        if len(v)==2 and v[1]-v[0]<=2: print((1)); break
        if len(v)==3 and (v[0]==v[1] or v[1]==v[2]): print((1)); break
        if len(v)==3 and (v[1]-v[0]<=2 or v[2]-v[1]<=2): print((1)); break
    else:
        print(2)

