import bisect
n=int(input())
a=[int(input()) for _ in range(n)][::-1]
dp=[]
for i in a:
  if bisect.bisect_right(dp,i)==len(dp):
    dp.append(i)
  else:
    dp[bisect.bisect_right(dp,i)]=i
print(len(dp))
