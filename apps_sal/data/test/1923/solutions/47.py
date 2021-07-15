_=input()
n=list(map(int,input().split()))
n.sort()
ans=0
for i in range(0,len(n),2):
  ans+=n[i]
print(ans)
