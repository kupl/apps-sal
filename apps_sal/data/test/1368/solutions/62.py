from math import factorial as f

def comb(n, r):
  return f(n) // (f(r) * f(n-r))

n, a, b = list(map(int, input().split()))
v = list(map(int, input().split()))

v.sort(reverse=True)

print((sum(v[:a])/a))

ans = 0
cnt0 = v.count(v[0])

if cnt0 >= a:
  for i in range(a, min(cnt0, b)+1):
    ans += comb(cnt0, i)
else:
  c = v[a-1]
  cnt1 = 0
  cnt2 = 0
  for i, vi in enumerate(v):
    if vi != c:
      continue
    if i < a:
      cnt1 += 1
    cnt2 += 1
  ans = comb(cnt2, cnt1)

print(ans)

