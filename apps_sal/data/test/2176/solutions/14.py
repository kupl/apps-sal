from sys import stdin
n=int(stdin.readline().strip())
s=[list(map(int,stdin.readline().strip().split())) for i in range(n)]
s1=[s[i][1] for i in range(n)]
s.sort()
s1.sort()
mod=998244353
x=1
ans=1
fact=[0 for i in range(n+1)]
fact[1]=1
for i in range(2,n+1):
    fact[i]=(i*fact[i-1])%mod
for i in range(1,n):
    if s[i][0]==s[i-1][0]:
        x+=1
    else:
        ans=(ans*fact[x])%mod
        x=1
ans=(ans*fact[x])%mod
t=True
for i in range(1,n):
    if s[i][1]<s[i-1][1]:
        t=False
        break
x=1
ans1=1
for i in range(1,n):
    if s1[i]==s1[i-1]:
        x+=1
    else:
        ans1=(ans1*fact[x])%mod
        x=1
ans1=(ans1*fact[x])%mod
if t:
    ans2=1
    x=1
    for i in range(1,n):
        if s[i]==s[i-1]:
            x+=1
        else:
            ans2=(ans2*fact[x])%mod
            x=1
    ans2=(ans2*fact[x])%mod
    ans=ans+ans1-ans2
else:
    ans+=ans1
print((fact[n]-ans)%mod)
    

