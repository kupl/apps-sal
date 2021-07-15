n,p=map(int,input().split())
s=input()
ans=0
if p==2 or p==5:
    for i in range(n):
        if int(s[i])%p==0:
            ans+=i+1
else:
    M=[0]*p
    M[0]=1
    tmp=0
    for i in range(n):
        tmp+=(int(s[-i-1])*pow(10,i,p))
        tmp%=p
        ans+=M[tmp]
        M[tmp]+=1
print(ans)
