MOD = 998244353
N = int(input())
if N == 1:
  print((1 * pow(2, MOD - 2, MOD)))
  return
if N == 2:
  print((1))
  print((1))
  return

ans = pow(2, N - 2, MOD) * N % MOD
q = pow(pow(2, N, MOD), MOD - 2, MOD)
for i in range(1, N):
  if i == 1:
    ans += 1
  else:
    ans = (ans + i * pow(2, i - 2, MOD) % MOD) % MOD 
for i in range(1, N):
  if i == N - 1:
    ans += N - 1
  else:
    ans = (ans + i * pow(2, N - 2 - i, MOD) % MOD) % MOD

t = ans * q % MOD
L = [t, t]
for i in range(2, (N + 1) // 2):
  ans = (ans + (i * 2 - 1) * pow(2, (i - 1) * 2 - 1, MOD) % MOD) % MOD
  L.append(ans * q % MOD)

for i in L:
  print(i)
L.reverse()
if N % 2 == 0:
  t = 0
else:
  t = 1
for i in L[t:]:
  print(i)

