from collections import Counter
N = int(input())

l = []
for i in range(1, N+1):
  while i % 2 == 0:
    l.append(2)
    i //= 2
  f = 3
  while f * f <= i:
    if i % f == 0:
      l.append(f)
      i //= f
    else:
      f += 2
  if i != 1:
    l.append(i)

c = Counter(l)
m = c.most_common()
c_75, c_25, c_15, c_5, c_3 = 0, 0, 0, 0, 0
for a in m:
  if a[1] >= 74:
    c_75 += 1
  if a[1] >= 24:
    c_25 += 1
  if a[1] >= 14:
    c_15 += 1
  if a[1] >= 4:
    c_5 += 1
  if a[1] >= 2:
    c_3 += 1
    
ans = c_75
ans += c_25 * (c_3-1)
ans += c_15 * (c_5-1)
ans += (c_5*(c_5-1)//2) * (c_3-2)
print(ans)
