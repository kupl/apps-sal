#     Codeforces Round #489 (Div. 2)
import collections
from functools import cmp_to_key
#key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )

import sys
def getIntList():
    return list(map(int, input().split()))    
import bisect
 
            
def getfactor(t):
    r = {}
    for x in range(2,100000):
        while t%x ==0:
            t = t//x
            if x not in r: r[x] = 1
            else:
                r[x] +=1
    if t> 1:
        r[t] = 1
    return r

L,R,X,Y = getIntList()

af = getfactor(X)
bf = getfactor(Y)
#print(af,bf)

base = X
res = set()
if X==Y :
    res.add( (X,Y))
for x in af:
    if x not in bf or af[x] > bf[x]:
        print(0)
        return
    bf[x] -= af[x]
    
z = [x for x in bf if bf[x] >0 ]
n = len(z)

def search(a,b, d):
    if d == n:
        res.add((a,b))
        return
    nt = z[d] ** bf[z[d]]
    search ( a * nt, b, d+1)
    search ( a , b* nt, d+1)
search(base,base,0)

r = 0
for x in res:
    if x[0] >=L and x[0] <=R and x[1] >=L and x[1] <=R: r+=1
print(r)

