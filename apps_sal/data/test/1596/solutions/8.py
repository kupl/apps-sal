import sys
input = sys.stdin.readline

S=input().strip()+"?"

if "m" in S or "w" in S:
    print(0)
    return

mod=10**9+7

DP0=[0]*(10**5+1)
DP1=[0]*(10**5+1)

DP0[1]=DP0[2]=1
DP1[2]=1

for i in range(3,10**5+1):
    DP0[i]=DP0[i-1]+DP1[i-1]
    DP1[i]=DP0[i-2]+DP1[i-2]
    DP0[i]%=mod
    DP1[i]%=mod

ANS=1
NOW="?"
count=0

for s in S:
    if s=="u" and NOW=="u":
        count+=1
    elif s=="u" and NOW!="u":
        if count!=0:
            ANS=ANS*(DP0[count]+DP1[count])%mod
        count=1
        NOW="u"

    elif s=="n" and NOW=="n":
        count+=1
    elif s=="n" and NOW!="n":
        if count!=0:
            ANS=ANS*(DP0[count]+DP1[count])%mod
        count=1
        NOW="n"

    else:
        if count!=0:
            ANS=ANS*(DP0[count]+DP1[count])%mod
        count=0
        NOW="?"

print(ANS)
        
        

