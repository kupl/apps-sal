import sys
input = sys.stdin.readline

n=int(input())
S=input().strip()

A=0
B=0
for s in S:
    if s=="(":
        A+=1
    else:
        B+=1

if A!=B:
    print(-1)
    return

NOW=[0]
for i in range(n):
    if S[i]==")":
        NOW.append((NOW[-1]-1))

    else:
        NOW.append((NOW[-1]+1))

score=0
ANS=0
for i in range(n+1):
    if NOW[i]<0:
        score+=1
    if NOW[i-1]<0 and NOW[i]==0:
        ANS+=score+1
        score=0
print(ANS)
        
        

