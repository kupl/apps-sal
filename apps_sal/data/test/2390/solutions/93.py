N,C=list(map(int,input().split()))

L=[]
for i in range(N):
    x,y=list(map(int,input().split()))
    L.append([x,y])
    
l=L[::-1]
L=[[0,0]]+L
R=[]

for i in range(N):
    R.append([C-l[i][0],l[i][1]])
R=[[0,0]]+R


#print(L)
#print(R)
TS=[0]
TW=[0]
RS=[0]
RW=[0]

for i in range(N):
    TS.append(TS[i]-L[i+1][0]+L[i][0]+L[i+1][1])
    TW.append(TW[i]-2*(L[i+1][0]-L[i][0])+L[i+1][1])
    RS.append(RS[i]-R[i+1][0]+R[i][0]+R[i+1][1])
    RW.append(RW[i]-2*(R[i+1][0]-R[i][0])+R[i+1][1])
    
MTS=[0]
MRS=[0]
for i in range(1,N+1):
    MTS.append(max(MTS[i-1],TS[i]))
    MRS.append(max(MRS[i-1],RS[i]))

ans=0
for i in range(N+1):
    if i>0 and L[i-1][0]*2>C:
        break
    else:
        if ans<TW[i] + MRS[N-i]:
            ans=TW[i] + MRS[N-i]
            
for i in range(N+1):
    if i>0 and R[i-1][0]*2>C:
        break
    else:
        if ans<RW[i]+MTS[N-i]:
            ans=RW[i]+MTS[N-i]
print(ans)

