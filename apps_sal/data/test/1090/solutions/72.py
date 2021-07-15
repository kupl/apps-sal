n,k=map(int,input().split())
s=input()
ans=0
for i in range(n-1):
  ans+=1 if s[i]==s[i+1] else 0
print(min(ans+2*k,n-1))
