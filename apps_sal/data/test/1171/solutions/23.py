n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for i in range(k+1):
  for j in range(k+1):
    if i+j > k or i+j > n:
      continue
    t = k-(i+j)
    s = v[:i] + v[(n-j):]
    s.sort()
    u = 0
    while u < t:
      u += 1
      if len(s) < 1:
        break
      if s[0] < 0:
        s.pop(0)
      else:
        break
    ans = max(ans, sum(s))
print (ans)
