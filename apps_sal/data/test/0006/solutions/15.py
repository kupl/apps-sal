from collections import defaultdict as DD
from bisect import bisect_left as BL
from bisect import bisect_right as BR
from itertools import combinations as IC
from itertools import permutations as IP
from random import randint as RI
import sys
MOD=pow(10,9)+7

def IN(f=0):
    if f==0:
        return ( [int(i) for i in sys.stdin.readline().split()] )
    else:
        return ( int(sys.stdin.readline()) )

tc=IN(1)
for _ in range(tc):
    n,x=IN()
    a=[]
    maxD=-1
    for i in range(n):
        f,y=IN()
        maxD=max(maxD,f)
        a.append(f-y)
    i=0
    a.sort(reverse=True)
    x=x-maxD
    if x<=0:
        print(1)
    else:
        if a[0]<=0:
            print(-1)
        else:
            r=x/a[0]
            if int(r)!=r:
                r = int(r)+1
            print(int(r+1))
        

