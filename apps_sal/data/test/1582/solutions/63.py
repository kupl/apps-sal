n = int(input())
t = [0] * 100
for i in range(11, 100):
  msb = i // 10
  lsb = i % 10
  if lsb == 0:
    continue
  for j in range(1, n+1):
    if j % 10 == lsb and int(str(j)[0]) == msb:
      t[i] += 1

ans = 0
for i in range(11, 100):
  msb = i // 10
  lsb = i % 10
  if lsb == 0:
    continue
  if msb == lsb:
    ans += t[i] ** 2
  else:
    ans += t[i] * t[lsb * 10 + msb]
print(ans)

