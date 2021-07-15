from collections import defaultdict
N,M,*A = map(int, open(0).read().split())
ls = [0]*10
ls[1] = 2
ls[2] = 5
ls[3] = 5
ls[4] = 4
ls[5] = 5
ls[6] = 6
ls[7] = 3
ls[8] = 7
ls[9] = 6
dic = defaultdict(int)
for a in A:
  k = ls[a]
  dic[k] = max(dic[k],a)
dp = [-1]*(N+1)
for k in dic.keys():
  if k>N:
    continue
  dp[k] = dic[k]
for i in range(N+1):
  for k in dic.keys():
    if i-k>0 and dp[i-k]!=-1:
      m = dp[i-k]*10+dic[k]
      dp[i] = max(dp[i], m)
print(dp[N])
