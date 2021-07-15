from collections import defaultdict as DD
from bisect import bisect_left as BL
from bisect import bisect_right as BR
from itertools import combinations as IC
from itertools import permutations as IP
from random import randint as RI
import heapq as HQ
import sys
MOD=pow(10,9)+7
def IN(f=0):
    if f==0:
        return ( [int(i) for i in sys.stdin.readline().split()] )
    else:
        return ( int(sys.stdin.readline()) )

tc=IN(1)
for _ in range(tc):
    n,r = IN()
    b = IN()
    b.sort()
    c=0
    #print(b)
    a=[-1]
    for i in range(0,n):
        if b[i]!=a[-1]:
            p=b[i]
            a.append(p)
    del a[0]
    #print(a)
        
    while(len(a)>0):
        if a[-1]-r*c<=0:
            break
        del a[-1]
        #print(a)
        c+=1
    print(c)
        
    
    
    

