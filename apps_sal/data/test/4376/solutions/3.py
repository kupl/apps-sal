
n,m=(list(map(int,input().strip().split(' '))))
arr=list((list(map(int,input().strip().split(' ')))))
dp=[arr[0]]
for i in range(1,n):
  dp.append(dp[i-1]+arr[i])
brr=list((list(map(int,input().strip().split(' ')))))
start = 0
for i in range(m):
  x=brr[i]
  for j in range(start,n):
    if(dp[j]>=brr[i]):
      if(j!=0):
        print(j+1,x-dp[j-1])
      else:
        print(j+1,x)
      start = j
      break

