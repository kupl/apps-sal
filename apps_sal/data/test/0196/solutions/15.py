#     Codeforces Round #489 (Div. 2)
import collections
from functools import cmp_to_key
#key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )

import sys
def getIntList():
    return list(map(int, input().split()))    

import bisect 
            
base = 10**9  + 7    
def get2k(k) :
    f = 2
    b = 1
    r = 1
    while k>=b:
        if k &b >0:
            r = r*f % base
        b*=2
        f = f*f % base
    return r

x, k = getIntList()
if x ==0:
    print(0)
    return
t2k = get2k(k)

r = x *   t2k *2 - t2k + 1
r = r% base
print(r)


