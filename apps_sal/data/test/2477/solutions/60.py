n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

def check(x):
  c = 0
  for i in range(n):
    c += a[i]//x
    if a[i]%x == 0:
      c -= 1
  if c <= k:
    return True
  else:
    return False

mx = max(a)
mn = 0
ans = [mx]
while mn <= mx:
  m = (mx+mn)//2
  if m == 0:
    if check(1):
      ans.append(1)
    break
  if check(m):
    mx = m - 1
    ans.append(m)
  else:
    mn = m + 1
print((min(ans)))

