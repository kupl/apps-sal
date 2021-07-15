def gyakugen(x,p):
  binp = str(bin(p-2))[::-1]
  ruijou = x
  
  result = 1
  for i in range(len(binp)-2):
    if binp[i] == "1":
      result *= ruijou
      result %= p
    ruijou *= ruijou
    ruijou %= mod
  return result

N, M = [int(i) for i in input().split()]
mod = 10**9+7

if abs(N-M) > 1 :
  print(0)
  return
elif N == M:
  ans = 1
  for i in range(1,N+1):
    ans *= i
    ans %= mod
    ans *= i
    ans %= mod
  ans *= 2
  ans %= mod
  print(ans)
else:
  ans = 1
  m = min(N,M)
  for i in range(1,m+1):
    ans *= i
    ans %= mod
    ans *= i
    ans %= mod
  ans *= max(N,M)
  ans %= mod
  print(ans)
