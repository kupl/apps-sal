MAXN = 55

f = [0] * MAXN
fac = [0] * MAXN

fac[0] = 1
for i in range(1, 51):
  fac[i] = fac[i - 1] * i

f[0] = 1;
for i in range(1, 51):
  f[i] += f[i - 1]
  for j in range(2, i + 1):
    f[i] += fac[j - 2] * f[i - j]

def my_fac(n):
  if n <= 0:
    return 1
  return fac[n]

def solve_first(n, k):
  ret = [0] * (n + 1)
  ret[1] = n
  for p in range(2, n + 1):
    for i in range(1, n + 1):
      if i in ret or i == p:
        continue
      ret[p] = i

      cur = p
      good = True
      for fuck in range(0, n - 1):
        cur = ret[cur]
        if cur == 0:
          good = True
          break
        if cur == p:
          good = False
          break
      
      if not good:
        ret[p] = 0
        continue

      k1 = my_fac(n - p - 1)
      if k > k1:
        k -= k1
      else:
        break
      ret[p] = 0
  ret.pop(0)
  assert len(ret) == n
  return ret;

def solve(n, k):
  if k == 1:
    ret = []
    for i in range(1, n + 1):
      ret.append(i)
    return ret

  tot = 0
  first = -1
  for i in range(1, n + 1):
    if tot + my_fac(i - 2) * f[n - i] >= k:
      first = i
      break;
    tot += my_fac(i - 2) * f[n - i]

  k -= tot
  cnt1 = my_fac(first - 1)
  cnt2 = f[n - first]
  
  x = k // cnt2 + 1
  y = k % cnt2

  if y == 0:
    y = cnt2
    x -= 1

  ret = solve_first(first, x)

  for v in solve(n - first, y):
    ret.append(v + first)

  return ret

T = int(input())

for t in range(0, T):
  s = input().split()
  n = int(s[0])
  k = int(s[1])
  if (k > f[n]):
    print("-1")
  else:
    ans = solve(n, k)
    for x in ans:
      print(x, end=" ")
    print("")
