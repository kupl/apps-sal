N=int(input())
s1=input()
s2=input()
ans=0
mod=10**9+7

if s1[0]==s2[0]:
    i=1
    ans+=3
    dual=False
else:
    i=2
    ans+=6
    dual=True
while i<N:
    if dual:
        if s1[i]==s2[i]:
            dual=False
        else:
            ans*=3
            ans%=mod
            i+=1
    else:
        ans*=2
        ans%=mod
        if s1[i]!=s2[i]:
            dual=True
            i+=1
    i+=1
print(ans%mod)
