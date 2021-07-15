import sys
input = sys.stdin.readline

def main():
  U = 2*10**6+2
  MOD = 10**9+7

  fact = [1]*(U+1)
  fact_inv = [1]*(U+1)

  for i in range(1,U+1):
      fact[i] = (fact[i-1]*i)%MOD
  fact_inv[U] = pow(fact[U], MOD-2, MOD)

  for i in range(U,0,-1):
      fact_inv[i-1] = (fact_inv[i]*i)%MOD

  def comb(n, k):
      if k < 0 or k > n:
          return 0
      z = fact[n]
      z *= fact_inv[k]
      z %= MOD
      z *= fact_inv[n-k]
      z %= MOD
      return z

  ans = 0
  r1, c1, r2, c2 = map(int, input().split())
  for i in range(c1, c2+1):
    ans += comb(i+r2+1, i+1) - comb(i+r1, i+1)
  print(ans%MOD)
  
def __starting_point():
  main()
__starting_point()
