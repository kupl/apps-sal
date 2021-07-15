n,c=map(int,input().split())
S=[]
for i in range(n):
    x,v=map(int,input().split())
    S.append([x,v])

F=[0]
rF=[0]
s=0
for i in range(n):
    s+=S[i][1]
    F.append(max(s-S[i][0],F[-1]))
    rF.append(max(s-2*S[i][0],rF[-1]))

S=list(reversed(S))
R=[0]
rR=[0]
s=0
for i in range(n):
    s+=S[i][1]
    R.append(max(s+S[i][0]-c,R[-1]))
    rR.append(max(s+2*(S[i][0]-c),rR[-1]))
    
R=list(reversed(R))
rR=list(reversed(rR))

ans=0
for i in range(n+1):
    ans=max(F[i]+rR[i],ans)
    ans=max(R[i]+rF[i],ans)
    
print(ans)
