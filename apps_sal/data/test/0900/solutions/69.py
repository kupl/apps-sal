S=input()
a=[0]*13
a[0]= 1

for c in S:
  dp=[0]*13
  for i in range(13):
    dp[(i*10)%13]=a[i]%(10**9+7)
  dp+=dp

  if c=='?':
    for i in range(13):
      a[i]=sum(dp[i+4:i+14])
  else:
    for i in range(13):
      a[i]=dp[i+13-int(c)]

print((a[5]%(10**9+7)))

