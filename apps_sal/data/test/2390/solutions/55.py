n,c=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
acumr=[0,arr[0][1]-arr[0][0]]
acuml=[0,arr[-1][1]-(c-arr[-1][0])]
for i in range(1,n):
  acumr.append(acumr[-1]+arr[i][1]-(arr[i][0]-arr[i-1][0]))
  acuml.append(acuml[-1]+arr[-(i+1)][1]-(arr[-i][0]-arr[-(i+1)][0]))
maxr=[0]
maxl=[0]
for i in range(1,n+1):
  maxr.append(max(maxr[-1],acumr[i]))
  maxl.append(max(maxl[-1],acuml[i]))
ans=0
for i in range(1,n+1):
  tmp1=acumr[i]
  tmp2=acuml[i]
  if arr[i-1][0]<maxl[n-i]:
    tmp1+=maxl[n-i]-arr[i-1][0]
  if c-arr[-i][0]<maxr[n-i]:
    tmp2+=maxr[n-i]-(c-arr[-i][0])
  ans=max(ans,tmp1)
  ans=max(ans,tmp2)
print(ans)
