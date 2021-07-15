def gcd_r(a, b):
  if memo[a][b] != 0:
    return memo[a][b]

  if a < b:
    a, b = b, a

  memo[a][b] = gcd(a, b)
  memo[b][a] = memo[a][b]
  return memo[a][b]

def gcd(a, b):
  r = a % b
  if r == 0:
    return b

  return gcd(b, r)

k = int(input())
memo = [[0]*(k+1) for _ in range(k+1)]
total = 0

for i in range(1, k+1, 1):
  for c in range(1, k+1, 1):
    total += gcd_r(gcd_r(i, i), c)

for a in range(1, k+1, 1):
  for b in range(a+1, k+1, 1):
    for c in range(1, k+1, 1):
      total += gcd_r(gcd_r(a, b), c) * 2

print(total)

