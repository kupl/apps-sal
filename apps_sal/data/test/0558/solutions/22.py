def main():
  ## IMPORT MODULE
  #import sys

  #sys.setrecursionlimit(100000)
  #input=lambda :sys.stdin.readline().rstrip()

  #f_inf=float("inf")
  MOD=998244353
  
  if 'get_ipython' in globals(): 
    ## SAMPLE INPUT
    n, m, k = 60522, 114575, 7559

  else:
    ##INPUT 
    #n = input()
    n, m, k = map(int, input().split())

  ## SUBMITION CODES HERE
  ans, N, K = 0, 1, 1
 
  for i in range(k+1):
    ans += N * pow(K, MOD-2, MOD) * pow(m-1, n-1-i, MOD)
    ans %= MOD
    N *= n-1-i
    N %= MOD
    K *= i+1
    K %= MOD
  
  ans *= m
  ans %= MOD
  print(ans)

main()
