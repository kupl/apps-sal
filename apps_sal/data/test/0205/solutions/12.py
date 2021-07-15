n,x=list(map(int,input().split()))

import math 
L=int(math.sqrt(x))

FACT=dict()

for i in range(2,L+2):
    while x%i==0:
        FACT[i]=FACT.get(i,0)+1
        x=x//i

if x!=1:
    FACT[x]=FACT.get(x,0)+1


ANS=float("inf")
for f in FACT:
    ANS_f=0
    x=f

    while x<=n:
        ANS_f+=n//x
        x*=f

    #print(f,ANS_f)

    ANS=min(ANS,ANS_f//FACT[f])

print(ANS)

    
    

