from sys import stdin
from collections import defaultdict
from time import time

P=829
MOD=2233333333333

def hashing(s,P,MOD) :
    h=0
    b=1
    for i in s :
        h+=b*ord(i)
        h%=MOD
        b*=P
        b%=MOD
    return h

def determine(w,lw) :
    return hashing(w,P,MOD) in mem[lw]

chars=['a','b','c']

n,m=list(map(int,input().split()))
S=time()
mem=defaultdict(set)
for i in range(n) :
    t=input()
    h0=hashing(t,P,MOD)
    lt=len(t)
    b=1
    for j in range(lt) :
        for c in chars :
            if not t[j]==c :
                #h=(h0+b*(ord(c)-ord(t[j])))%MOD
                mem[lt].add((h0+b*(ord(c)-ord(t[j])))%MOD)
        b*=P
        b%=MOD

prt=[]
for i in range(m) :
    w=input()
    lw=len(w)
    if lw not in mem :
        prt.append('NO')
        continue
    if determine(w,lw) :
        prt.append('YES')
    else :
        prt.append('NO')

print('\n'.join(prt))

#print((time()-S)*1000)

