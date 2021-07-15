n, t, c = map(int, input().split())
a = list(map(int, input().split()))
s = [0 for i in a]
h = 0
l = 0
def push(i):
  nonlocal h, l, s, a
  while h < l and a[s[l - 1]] <= a[i]:
    l -= 1
  s[l] = i
  l += 1
for i in range(c):
  if a[i] > t:
    push(i)
if h == l:
  ans = 1
else:
  ans = 0
for i in range(c, n):
  if h < l and i - c == s[h]:
    h += 1
  if a[i] > t:
    push(i)
  if h == l:
    ans += 1
print(ans)
