n=int(input())
p=list(map(int,input().split()))
ans=0
count=0
for i in range(n):
  if p[i] == i+1:
    ans+=1
    count+=1
  else:
    count=0
  if count==2:
    ans-=1
    count=0
print(ans)
