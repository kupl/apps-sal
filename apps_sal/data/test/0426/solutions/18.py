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

n,k=IN()
s=input()
s=[int(i) for i in s]
r=""
i=0
p=0
if len(s)==1 and k>0:
    print(0)
elif len(s)==1 and k==0:
    print(s[0])
else:
    while(i<n and p<k):
        if i==0:
            if s[i]!=1:
                s[i]=1
                p+=1
        else:
            if s[i]!=0:
                s[i]=0
                p+=1
        i+=1
    r=[str(i) for i in s]
    print(''.join(r))
        
        
    
    

