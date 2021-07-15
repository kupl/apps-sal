'''
Created on 2020/08/23

@author: harurun
'''
def main():
  from collections import Counter
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  ans=0
  N=int(pin())
  A=list(map(int,pin().split()))
  c=Counter(A)
  t=max(A)
  dp=[True]*t
  for i in A:
    if dp[i-1]:
      n=2*i
      while n<=t:
        dp[n-1]=False
        n+=i
  for k in A:
    if c[k]==1 and dp[k-1]:
      ans+=1
  print(ans)
  return
main()

