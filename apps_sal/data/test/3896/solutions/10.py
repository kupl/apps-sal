MOD = 1000000007

s = input()
n = len(s)
p = [1]
for i in range(301):
  p.append((2*p[-1]) %MOD)


res = 0
m = n
g = 0
for i in range(n):
  if s[i] == '1':
    res += (p[g] * (p[2*m-2]%MOD)) % MOD
    res = res % MOD
  g += 1
  m -= 1
  
print(res)
