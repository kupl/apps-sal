import math
import sys
n=int(input())
cnt=0
cn=0
for i in range(n):
    a,b=list(map(int,input().split()))
    if a<0:cnt+=1
    else:cn+=1
if cn==1 or cnt==1 or cnt==0 or cn==0:
    print('Yes')
else:print('No')

