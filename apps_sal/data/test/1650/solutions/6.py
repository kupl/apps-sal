S=input()
c=len(S)
mod=1000000007
p=1
ans=pow(3,c-1,mod)
for i in range(1,c):
  if S[i]=="1":
    ans+=pow(2,p,mod)*pow(3,c-i-1,mod)
    p+=1
print((ans+pow(2,p,mod))%mod)
