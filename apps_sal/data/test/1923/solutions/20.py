N=int(input())
L=sorted(list(map(int,input().split())),reverse=True)
ans=0
for i in range(1,len(L),2):
  ans+=min(L[i],L[i-1])
print(ans)

