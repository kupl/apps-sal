import sys
input = sys.stdin.readline

x=int(input())
y=x
ANS=x+1
AX=[0,0]

import math
L=int(math.sqrt(x))

FACT=dict()

for i in range(2,L+2):
    while x%i==0:
        FACT[i]=FACT.get(i,0)+1
        x=x//i

if x!=1:
    FACT[x]=FACT.get(x,0)+1
x=y
LEN=len(FACT)
LIST=list(FACT.keys())
for i in range(1<<LEN):
    sc=1
    for j in range(LEN):
        if i & (1<<j) !=0:
            sc*=LIST[j]**FACT[LIST[j]]

    if ANS>max(sc,x//sc):
        ANS=max(sc,x//sc)
        AX=[sc,x//sc]

print(*AX)

