import sys
input = sys.stdin.readline

mod=998244353

n=int(input())
S=[list(map(int,input().split())) for i in range(n)]

FACT=[1]
for i in range(1,3*10**5+10):
    FACT.append(FACT[-1]*i%mod)

X=[x for x,y in S]
Y=[y for x,y in S]

ANS=1
for i in range(1,n+1):
    ANS=ANS*i%mod

X.sort()
XA=1
count=1
for i in range(1,n):
    if X[i]==X[i-1]:
        count+=1
    else:
        XA=XA*FACT[count]%mod
        count=1
        
XA=XA*FACT[count]%mod

Y.sort()
YA=1
count=1
for i in range(1,n):
    if Y[i]==Y[i-1]:
        count+=1
    else:
        YA=YA*FACT[count]%mod
        count=1
YA=YA*FACT[count]%mod


S.sort()
SA=1
count=1
for i in range(1,n):
    if S[i][1]<S[i-1][1]:
        SA=0
        break
    
    if S[i]==S[i-1]:
        count+=1
    else:
        SA=SA*FACT[count]%mod
        count=1

SA=SA*FACT[count]%mod

    

print((ANS-XA-YA+SA)%mod)

