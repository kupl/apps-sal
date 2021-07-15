W,H,N=map(int,input().split())
A,B,C,D=[0],[W],[0],[H]

for i in range(N):
    x,y,a=map(int,input().split())
    if a==1:
        A.append(x)
    elif a==2:
        B.append(x)
    elif a==3:
        C.append(y)
    elif a==4:
        D.append(y)

W=min(B)-max(A)
H=min(D)-max(C)

if W<0 or H<0:
    ans=0
else:
    ans=H*W
print(ans)
