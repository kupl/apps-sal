l ,r = list(map(int, input().split()))
t = []
if r-l >= 2019:
  print((0))
  return
elif r-l < 2019:
  if 2019 <= l:
    for i in range(l, r):
      for j in range(i+1, r+1):
        ii = i % 2019
        jj = j % 2019
        s = (ii*jj) % 2019
        t.append(s)
    ans = min(t)
    print(ans)
  elif l < 2019 < r:
    for i in range(l, r):
      for j in range(i+1, r+1):
        ii = i % 2019
        jj = j % 2019
        s = (ii*jj) % 2019
        t.append(s)
    ans = min(t)
    print(ans)
  elif r <= 2019:
    for i in range(l, r):
      for j in range(i+1, r+1):
        s = (i*j) % 2019
        t.append(s)
    ans = min(t)
    print(ans)

