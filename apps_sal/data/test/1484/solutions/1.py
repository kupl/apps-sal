import sys
input = sys.stdin.readline

mod=998244353

n,k=list(map(int,input().split()))
A=list(map(int,input().split()))


A0=[A[i] for i in range(n) if i%2==0]
A1=[A[i] for i in range(n) if i%2==1]

for j in range(1,len(A0)):
    if A0[j]!=-1 and A0[j]==A0[j-1]:
        print(0)
        return

for j in range(1,len(A1)):
    if A1[j]!=-1 and A1[j]==A1[j-1]:
        print(0)
        return

        
    
OPENLIST=[]

j=0
L=len(A0)
while j<L:
    OPEN=CLOSE=-10
    if A0[j]==-1:
        if j==0:
            OPEN=-11
        else:
            OPEN=A0[j-1]
            
        COUNT=0
        while A0[j]==-1:
            COUNT+=1
            j+=1

            if j==L:
                CLOSE=-11
                break

        if OPEN==-11 and CLOSE==-11:
            OPENLIST.append([COUNT,0])
        elif OPEN==-11 or CLOSE==-11:
            OPENLIST.append([COUNT,1])
        else:
            if A0[j]==OPEN:
                OPENLIST.append([COUNT,3])
            else:
                OPENLIST.append([COUNT,2])

    else:
        j+=1
j=0
L=len(A1)
while j<L:
    OPEN=CLOSE=-10
    if A1[j]==-1:
        if j==0:
            OPEN=-11
        else:
            OPEN=A1[j-1]
            
        COUNT=0
        while A1[j]==-1:
            COUNT+=1
            j+=1

            if j==L:
                CLOSE=-11
                break

        if OPEN==-11 and CLOSE==-11:
            OPENLIST.append([COUNT,0])
        elif OPEN==-11 or CLOSE==-11:
            OPENLIST.append([COUNT,1])
        else:
            if A1[j]==OPEN:
                OPENLIST.append([COUNT,3])
            else:
                OPENLIST.append([COUNT,2])

    else:
        j+=1

ANS=1
for x,y in OPENLIST:
    if y==0:
        ANS=ANS*k*pow(k-1,x-1,mod)%mod

    elif y==1:
        ANS=ANS*pow(k-1,x,mod)%mod

    elif y==2:
        DP0=0
        DP1=1

        for r in range(x+1):
            NDP0=DP1
            NDP1=(DP0*(k-1)+DP1*(k-2))%mod

            DP0=NDP0
            DP1=NDP1



        ANS=ANS*DP0%mod

    else:
        DP0=1
        DP1=0

        for r in range(x+1):
            NDP0=DP1
            NDP1=(DP0*(k-1)+DP1*(k-2))%mod

            DP0=NDP0
            DP1=NDP1



        ANS=ANS*DP0%mod
        
            

print(ANS)
        


        
        


