#     Codeforces Round #489 (Div. 2)
import collections
from functools import cmp_to_key
#key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )

import sys
def getIntList():
    return list(map(int, input().split()))    

import bisect 
            
    
 
n,  = getIntList()

z = getIntList()

res = set()
for x in z:
    if x !=0:
        res.add(x)
    
print(len(res))

