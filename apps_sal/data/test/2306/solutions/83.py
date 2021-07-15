N = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
def exe(x, y, z, t):
  ans = t * y
  if x < y:
    ans -= (y - x) * (y - x) / 2
  if y > z:
    ans -= (y - z) * (y - z) / 2
  return ans

def upd(x, y, z, t):
  a = y - x
  b = y - z
  if y > z:
    if t < a:
      y = x + t
    elif t < a + b:
      y = x + (t + (z - x)) / 2
  else:
    if t < a:
      y = x + t
  return y

v = [0] + v + [0]
L = [0] * len(v)
v[1] = upd(v[0], v[1], v[2], t[0])
v[-2] = upd(v[-1], v[-2], v[-3], t[-1])
for i in range(1, N):
  k = -1
  for j in range(1, N + 1):
    if L[j] == 0:
      if k == -1:
        k = j
      else:
        if v[j] < v[k]:
          k = j
  L[k] = 1
  if k != 1:
    v[k - 1] = upd(min(v[k], v[k - 2]), v[k - 1], max(v[k], v[k - 2]), t[k - 2])
  if k != N:
    v[k + 1] = upd(min(v[k], v[k + 2]), v[k + 1], max(v[k], v[k + 2]), t[k])

ans = 0
for i in range(N):
  ans += exe(v[i], v[i + 1], v[i + 2], t[i])

print(ans)
