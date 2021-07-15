n,k=list(map(int,input().split()))

s=[]
for i in range(1,n+1):
  s.append(i%k)

from collections import Counter
dic=Counter(s)

ans=0
for a in dic:
  if (2*a)%k==0:
    ans=ans+dic[a]*dic[(k-a)%k]*dic[(k-a)%k]
    
print(ans)

  
  


