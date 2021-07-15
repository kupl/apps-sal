n, k = map(int, input().split())
a = list(map(int, input().split()))
p = 1
t = [1]
u = set()
u.add(1)
for i in range(n):
  p = a[p - 1]
  if p not in u:
    t.append(p)
    u.add(p)
  else:
    break
c = t.index(p)
r = len(t) - c
if k < len(t):
  ans = t[k]
else:
  if (k - c + 1) % r == 0:
    ans = t[-1]
  else:
    ans = t[(k - c + 1) % r + c - 1]
print(ans)
