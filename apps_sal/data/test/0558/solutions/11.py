N, M, K = map(int, input().split())
mod = 998244353

b = str(bin(mod-2))[2:]
blis = []
for _ in range(len(b)):
  if b[-_-1] == '1':
    blis.append(_)

def modinv(a):
  if a == 1:
    return 1
  else:
    res = 1
    n = len(b)
    li = []
    for _ in range(n):
      li.append(a%mod)
      a = a*a%mod
    for item in blis:
      res = res * li[item] %mod
    return res
"""      
inv = [0,1]
for i in range(2, N):
  inv.append((-inv[mod%i]*(mod//i))%mod)
"""
if N == 1:
  print(M)
  return

m = [1]
s = 1
for _ in range(N-1):
  s = s*(M-1)%mod
  m.append(s)

ncombi = [1]
c = 1
for k in range(K):
  c = c*(N-1-k)*modinv(k+1)
  c %= mod
  ncombi.append(c)

"""
olis = ncombi
for k in range(N-1):
  nlis = [1]
  for  j in range(len(olis)-1):
    nlis.append(olis[j]+olis[j+1])
  nlis.append(1)
  olis = nlis
  #print(olis)
ncombi = olis
"""
ans = 0
for k in range(K+1):
  ans = ans + m[-k -1]*ncombi[k]
  ans %= mod

ans = ans*M%mod

print(ans)
