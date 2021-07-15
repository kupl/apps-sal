import sys
input = sys.stdin.readline

x=int(input())

if x==1:
    print(1)
    return

import math 
L=int(math.sqrt(x))

FACT=dict()

for i in range(2,L+2):
    while x%i==0:
        FACT[i]=FACT.get(i,0)+1
        x=x//i

if x!=1:
    FACT[x]=FACT.get(x,0)+1

if len(FACT)>1:
    print(1)
else:
    print(list(FACT.keys())[0])

