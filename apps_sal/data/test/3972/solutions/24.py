import sys
sys.setrecursionlimit(10**7)
def main1(n):
  # DP メモ化再帰 O(N^2)
  mod=10**9+7
  ret=0
  memo={}
  memo[n-1]=n
  #memo[i]:idx=iに何を書き込むか検討しているとき、i以降の数列の種類数
  def func(i):
    if i in memo:return memo[i]
    if i>n-1:return 1
    ret=0
    # iに1を書き込む
    ret+=func(i+1)
    for k in range(2,n+1):
      # iにkを書き込み、その次に1を書き込む。
      ret+=func(i+k+1)
      # iにkを書き込み、その次に2以上を書き込む。
      ret+=n-1
      ret%=mod
    memo[i]=ret
    return ret
  ret=func(0)
  for k in memo:print((k,memo[k]))
  return ret

# 累積和で高速化できる。memo[i]をiの大きい順に数える
def main2(n):
  # DP O(N)
  mod=10**9+7
  # dp[i]:=idx=iに何を書き込むか検討しているとき、i以降の数列の種類数
  dp=[1]*(2*n)
  dp[n-1]=n
  dp[n-2]=n**2
  now=n-1
  for i in range(n-3,-1,-1):
    # 1を書き込む
    dp[i]=dp[i+1]
    now-=dp[i+n+1]
    now+=dp[i+3]
    dp[i]+=now
    #for k in range(2,n+1):# i+3~i+n+1の和
    #  dp[i]+=dp[i+k+1]
    #  dp[i]%=mod
    dp[i]+=(n-1)**2
    dp[i]%=mod
  return dp[0]
def __starting_point():
  n=int(input())
  ret2=main2(n)
  print(ret2)


__starting_point()
