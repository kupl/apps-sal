comb_memo = {}
def comb(n, r):
  nonlocal comb_memo
  if (n, r) in comb_memo:
    return comb_memo[(n, r)]
  else:
    r = min(r, n-r)
    res = 1
    for _ in range(r):
      res *= n
      n -= 1
    for i in range(1, r+1):
      res //= i
    comb_memo[(n, r)] = res
    comb_memo[(n, n-r)] = res
    return res

N, A, B = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)

mu = sum(v[:A]) / A
ans = 0
if v[0] == mu:
  R = v.count(v[0])
  for i in range(A, B+1):
    if i > R:
      break
    ans += comb(R, i)
else:
  min_v = v[A-1]
  n = v.count(min_v)
  need = v[:A].count(min_v)
  ans += comb(n, need)

print(mu)
print(ans)
