N=int(input())
S=[input() for _ in range(N)]
cnt=[0]*N
cnt2=[]
flag=0

if len(S)>1:
    for i in range(N):
        if S[i][0]=='M':
            cnt[0]+=1
        elif S[i][0]=='A':
            cnt[1]+=1
        elif S[i][0]=='R':
            cnt[2]+=1
        elif S[i][0]=='C':
            cnt[3]+=1
        elif S[i][0]=='H':
            cnt[4]+=1

for i in range(N):
    if cnt[i]!=0:
        cnt2.append(cnt[i])
        
import math
import itertools
ans=0

for v in itertools.combinations(cnt2, 3):
    ans+=v[0]*v[1]*v[2]

print(ans)
