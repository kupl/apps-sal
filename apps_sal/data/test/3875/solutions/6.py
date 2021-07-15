from bisect import bisect_left
def LIS(N, A):
  A = list(A)
  lis = []
  for i in range(N):
    ind = bisect_left(lis,A[i])
    if ind == len(lis):
      lis.append(A[i])
    else:
      lis[ind] = A[i]
  return len(lis)

def comb(n,r):
  if not 0<=r<=n:
    return 0
  ans = 1
  for i in range(r):
    ans *= n-i
  for i in range(r):
    ans //= i+1
  return ans

def compress(arr):
  XS = list(set(arr))
  XS.sort()
  dic = {e: i for i, e in enumerate(XS)}
  for i in range(len(arr)):
    arr[i] = dic[arr[i]]
  return arr

from itertools import groupby, accumulate, product, permutations, combinations
N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
from collections import defaultdict
def gutyoku(N,A):
  cnt = 0
  for a in range(1,A[0]+1):
    if N==1:
      B = [a]
      cnt += LIS(N,B)
      continue
    for b in range(1,A[1]+1):
      if N==2:
        B = [a,b]
        cnt += LIS(N,B)
        continue
      for c in range(1,A[2]+1):
        if N==3:
          B = [a,b,c]
          cnt += LIS(N,B)
          continue
        for d in range(1,A[3]+1):
          if N==4:
            B = [a,b,c,d]
            cnt += LIS(N,B)
            continue
          for e in range(1,A[4]+1):
            if N==5:
              B = [a,b,c,d,e]
              cnt += LIS(N,B)
              continue
            for f in range(1,A[5]+1):
              B = [a,b,c,d,e,f]
              cnt += LIS(N,B)
  return cnt
def solve(N,A):
  ans = 0
  dic = defaultdict(lambda: 0)
  # debug = defaultdict(lambda: [0,0])
  for pro in product([0,1],repeat=N-1):
    lis = [1]*N
    pro = list(pro)
    for i in range(N-1):
      lis[i+1] = lis[i]+pro[i]
    for perm in permutations(lis,N):
      if dic[perm]==1:
        continue
      dic[perm] = 1
      num = max(perm)
      lis2 = [0]+[10**10]*num
      for i,p in enumerate(perm):
        lis2[p] = min(lis2[p],A[i])
      for i in range(num-1,0,-1):
        lis2[i] = min(lis2[i], lis2[i+1])
      # cnt = 0
      # j = 0
      # cum = 1
      # for i in range(1,num+1):
      #   if lis2[i]-lis2[j]==0:
      #     continue
      #   if j-1>=0:
      #     cum *= comb(lis2[i-1]-lis2[j-1],i-j)
      #   cnt += cum*comb(lis2[i]-lis2[j],num+1-i)
      #   j = i
      comp = lambda arr: {i: e for i, e in enumerate(sorted(set(arr)))}
      compdic = comp(lis2)
      complis2 = compress(lis2[:])
      M = max(complis2)
      dp = [[0]*(M+1) for _ in range(num+1)]
      dp[0][0] = 1
      for i in range(1,num+1):
        for j in range(1,complis2[i]+1):
          for k in range(j):
            dp[i][j] += dp[i-1][k]*(compdic[j]-compdic[j-1])
          for k in range(i-1,0,-1):
            if complis2[k]<j:
              break
            dp[i][j] += sum(dp[k-1][:j])*comb(compdic[j]-compdic[j-1], i-k+1)
      ans += sum(dp[-1])*LIS(N,perm)
      # debug[tuple(lis2)][0] = sum(dp[-1])
      # debug[tuple(lis2)][1] += LIS(N,perm)
      # print(list(perm),lis2,sum(dp[-1]),LIS(N,perm))
  # for k,v in debug.items():
    # print(k,v)
  return ans
# ans1 = gutyoku(N,A)
ans2 = solve(N,A)
for i in range(N):
  ans2 *= pow(A[i],mod-2,mod)
  ans2 %= mod
print(ans2)
# if ans1!=ans2:
  # print(ans1,ans2)


