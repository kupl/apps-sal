N,Q=list(map(int,input().split()))
S=input()
li=[0]
A=False
ans=0
import copy
for i in range(N):
    if A==True:
        if S[i]=="C":
            ans+=1
        A=False
    if S[i]=="A":
        A=True
    li.append(copy.copy(ans))
for j in range(Q):
    a,b=list(map(int,input().split()))
    print((li[b]-li[a]))

