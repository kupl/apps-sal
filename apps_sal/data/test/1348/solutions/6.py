import os
import sys
import copy

# sys.stdin = open(os.path.join(os.path.dirname(__file__), '7.in'))

n,k = map(lambda x:int(x), input().split())
# G = [[-1 for _ in range(n+1)] for _ in range(n+1)]
C = [0 for _ in range(n+1)]
d = [ {'d':int(_),'idx':i+1} for i, _ in enumerate(input().split())]
d.sort(key = lambda x: x['d'])

# print(d)
pos = True
eg = 0
reeg = []
# multi zero number
cz = 0
for dis in d:
    if dis['d'] == 0:
        cz += 1 

if cz != 1:
    pos= False
else:
    first = True
    c_vertex = -1
    Preidx = 0
    PPreidx = 0
    pd = 2<<30
    for i,vx in enumerate(d):
        if i == 0 :
            c_vertex = vx['idx']
            pd = 0
            continue   
        # print(vx)
        find = False
        if vx['d'] == pd:
            vvbg= PPreidx
        else:
            vvbg = Preidx
        # print("ss",vx,d[vvbg],PPreidx,Preidx)
        
        while vvbg < i:
            # print("ss",vx,d[vvbg])
            if C[d[vvbg]['idx']] < k:
                if d[vvbg]['d'] + 1 != vx['d']:
                    pos = False
                    break
                # G[d[vvbg]['idx']][vx['idx']] = 1
                C[d[vvbg]['idx']] += 1
                C[vx['idx']] += 1
                eg += 1
                find = True
                reeg.append((d[vvbg]['idx'],vx['idx']))
                break
            # else:
            #     Preidx += 1
            vvbg += 1
                # print(reeg)
        if not find:
            pos = False

        if i >= 1 and vx['d'] != pd:
            # print("ppre", Preidx, PPreidx)
            PPreidx = Preidx
            Preidx=i
        pd = vx['d']
        
if pos:
    print(eg)
    for a,b in reeg:
        print(a,b)
else:
    print(-1)
