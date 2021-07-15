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

n,m=IN()
a=[]
b=[]
c=[]
for i in range(n):
    rr=IN()
    a.append(rr)
    c.append(rr)
for i in range(n):
    b.append(IN())

fr=[0 for i in range(n)]
fc=[0 for i in range(m)]

for i in range(n):
    for j in range(m):
        if c[i][j]==b[i][j]:
            c[i][j]=0
        else:
            c[i][j]=1
            fr[i]+=1
            fc[j]+=1
f="Yes"
for i in fr:
    if i%2!=0:
        f="No"
        break
for i in fc:
    if i%2!=0:
        f="No"
        break
print(f)

            

