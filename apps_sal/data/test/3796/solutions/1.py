import sys
input = sys.stdin.readline
 
n=int(input())
A=list(map(int,input().split()))

from collections import Counter
 
C=Counter(A)

import math

MAXV=max(max(C.values()),int(math.sqrt(n)))
 
VCOUNT=[0]*(MAXV+1)
 
for v in list(C.values()):
    VCOUNT[v]+=1
    
SUM=n
 
from itertools import accumulate
 
ACC=list(accumulate(VCOUNT[::-1]))[::-1]
 
 
ANS=0
 
for i in range(MAXV,0,-1):
    if SUM//i>=i:
        if ANS<i*(SUM//i):
            ANS=i*(SUM//i)
            ANSX=i,(SUM//i)
 
    SUM-=ACC[i]
 
print(ANS)
 
X,Y=ANSX[0],ANSX[1]
print(X,Y)
 
A=[[0]*Y for i in range(X)]
 
i=0
j=0
nowj=0
colored=0
same=0
LIST=list(C.most_common())
ind=0
 
while colored<ANS:
    A[i][j],MAX=LIST[ind]
    colored+=1
    i+=1
    j=(j+1)%Y
    if i==X:
        i=0
        nowj+=1
        j=nowj
    same+=1
 
    if same==min(X,MAX):
        ind+=1
        same=0
 
for a in A:
    sys.stdout.write(" ".join(map(str,a))+"\n")

