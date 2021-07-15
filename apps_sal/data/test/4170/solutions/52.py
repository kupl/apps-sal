n=int(input())
h=list(map(int,input().split()))
h.append(10**9+1)
ans=cnt=0
for i in range(n):
  if h[i]>=h[i+1]:
    cnt+=1
  else:
    ans=max(ans,cnt)
    cnt=0
print(ans)
