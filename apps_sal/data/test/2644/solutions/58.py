N=int(input())
P=list(map(int,input().split()))
ans=[]
l,r=0,0
for i in range(N):
  if P[i]==r+1:
    r=i
    for j in range(r,l,-1):
      P[j-1],P[j]=P[j],P[j-1]
      ans.append(j)
    l=r
  
if P!=sorted(P) or len(ans)!=N-1:
  print(-1);return
print(*ans,sep="\n")
