n=int(input())
p=list(map(int,input().split()))
cnt=0
for i in range(1,n+1):
  if p[i-1]!=i:
    cnt+=1
if cnt==0 or cnt==2:
  print("YES")
else:
  print("NO")
