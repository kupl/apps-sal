N, M = list(map(int, input().split()))

Msq = int(M**(1/2)) + 2
yaku = []

for i in range(2, Msq):
  now = 0
  while M%i == 0:
    M = M//i
    now += 1
  if now >= 1:
    yaku.append(now)
    
if M > 1:
  yaku.append(1)
  
yaku.sort()

MOD = 1000000007
frac = [1] * (N+50)
num = len(frac)
for i in range(num-1):
  frac[i+1] = frac[i] * (i+1) % MOD
  
finv = [1] * (N+50)
finv[-1] = pow(frac[-1], MOD-2, MOD)
for i in range(1, num):
  finv[num-1-i] = finv[num-i] * (num-i) % MOD
  
ans = 1
for i in yaku:
  ans = ans * frac[N+i-1] * finv[N-1] * finv[i] % MOD
  
print(ans)

