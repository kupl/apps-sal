import sys
input = sys.stdin.readline
from collections import deque

S=input().strip()


LEN=len(S)
i=1
j=0
A=[0]*LEN
A[0]=LEN

while i<LEN:
    while i+j<LEN and S[j]==S[i+j]:
        j+=1
    A[i]=j
    
    if j==0:
        i+=1
        continue
    
    k=1
    while i+k<LEN and k+A[k]<j:
        A[i+k]=A[k]
        k+=1
    i+=k
    j-=k

ANS=[0]*(LEN+1)

for a in A:
    ANS[a]+=1

for i in range(LEN-1,-1,-1):
    ANS[i]+=ANS[i+1]

ANS2=[]
for i in range(1,LEN+1):
    if A[LEN-i]==i:
        ANS2.append((i,ANS[i]))

print(len(ANS2))
for x,y in ANS2:
    print(x,y)




