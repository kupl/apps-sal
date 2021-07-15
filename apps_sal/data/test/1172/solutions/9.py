mod = 1000000007
s = input()
al = 0
cr = s.count('C')
ql = 0
qr = s.count('?')
ans = 0
for c in s:
  if c == 'C':
    cr -= 1
  elif c == '?':
    qr -= 1
    ans += (3 * al + ql) * (3 * cr + qr) * pow(3, ql + qr + mod - 3, mod)
    ans %= mod
    ql += 1
  elif c == 'B':
    ans += (3 * al + ql) * (3 * cr + qr) * pow(3, ql + qr + mod - 3, mod)
    ans %= mod
  else:
    al += 1
print(ans)

