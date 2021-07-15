from collections import deque

poe=deque([])
S=input()
for i in range(len(S)):
    poe.append(S[i])
Q=int(input())
P=[]
cnt=0
for i in range(Q):
    a=list(input().split())
    P.append(a)

for i in range(Q):
    if len(P[i])==1:
        cnt+=1
    else:
        P[i][1]=int(P[i][1])+cnt
        if P[i][1]%2==1:
            poe.appendleft(P[i][2])
        else:
            poe.append(P[i][2])

poe=list(poe)
if cnt%2==1:
    poe=poe[::-1]
print(''.join(poe))
