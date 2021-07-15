H, W, A, B = list(map(int, input().split()))

MOD = 1000000007

fac = [1, 1]
inverse = [0, 1]
ifac = [1, 1]
  
for i in range(2, H+W):
  fac.append((fac[-1] * i) % MOD)
  inverse.append((-inverse[MOD % i] * (MOD // i))  % MOD)
  ifac.append((ifac[-1] * inverse[i]) % MOD)

def f(n):
  return fac[B+n+H-A-1] * fac[W-B-1-n+A-1] * ifac[B+n] * ifac[H-A-1] * ifac[W-B-1-n] * ifac[A-1]

def sigma(func, frm, to):
  result = 0
  for i in range(frm, to+1):
    result += func(i)
  return result
 
print((sigma(f, 0, W-B-1)%MOD))

