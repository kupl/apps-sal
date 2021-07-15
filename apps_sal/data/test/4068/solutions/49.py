N, M = map(int, input().split())
MOD = 10 ** 9 + 7
s = 0

def comb(n, k):
  if k > n - k:
    k = n - k
  de = 1
  nu = 1
  for i in range(k):
    de *= (n - i)
    de = de % MOD
    nu *= (i + 1)
    nu = nu % MOD
  nu = pow(nu, -1, MOD)
  return (de * nu) % MOD

def calc_from_step(step):
  temp = 0
  for i in range(1 + (step // 2)):
    temp += comb(step-i, i)
  return temp


arr = [1, 1]
steps = []
step = 0
s = 0
for i in range(M):
  l = int(input()) - 1
  steps.append(l-s)
  if s > l:
    print(0)
    return
  if step < l - s:
    step = l - s
  s = l + 2
l = N
steps.append(l-s)
if step < l - s:
  step = l - s

for i in range(step - 1):
  arr.append((arr[i] + arr[i+1])%MOD)
ans = 1

for i in steps:
  ans *= arr[i]
  ans = ans % MOD
print(ans)
