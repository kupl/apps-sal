def main():
  N,M=map(int,input().split())
  A=[0]*M
  import heapq
  import collections
  from itertools import permutations
  table=collections.defaultdict(list)
  AC=[[0,0] for i in range(M)]
  C=[set() for i in range(M)]
  for i in range(M):
    a,b=map(int,input().split())
    AC[i][0]=a
    tmp=set(map(int,input().split()))
    for x in tmp:
      AC[i][1] |= 1<<(x-1)
  dp=[10**9]*(2**N)
  dp[0]=0

  for i in range(1,2**N):
    k=0
    s=set()
    for j in range(1,i):
      if i & j == j:
        dp[i]=min(dp[i],dp[j]+dp[i^j])
    for a,c in AC:
      if c&i == i:
        dp[i]=min(dp[i],a)
    #print(dp[i],bin(i))

  if dp[-1]==10**9:
    print(-1)
  else:
    print(dp[-1])
main()
