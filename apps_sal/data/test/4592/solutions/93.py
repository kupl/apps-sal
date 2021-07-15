def factrial(n):
  factors = []
  while n%2 == 0:
    factors.append(2)
    n //= 2
    
  for i in range(3, int(n**0.5)+1, 2):
    while n%i == 0:
      factors.append(i)
      n //= i
      
  if n != 1: factors.append(n)
    
  return factors


n = int(input())
mod = 10**9+7

d = {}
for i in range(1,n+1):
  fac = factrial(i)
  for j in fac:
    if j in d: d[j] += 1
    else: d[j] = 1

ans = 1
for k,v in d.items():
  ans *= (v+1)
  ans %= mod
print(ans)
