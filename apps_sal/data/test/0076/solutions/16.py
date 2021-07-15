#     Educational Codeforces Round 45 (Rated for Div. 2)
import collections
from functools import cmp_to_key
#key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )

import sys
def getIntList():
    return list(map(int, input().split()))    

 
            
    
n,m, a,b = getIntList()

z = n%m

r = min( (m-z) * a ,  z * b)


print(r)

