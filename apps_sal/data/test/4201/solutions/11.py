import itertools
h, w, k = map(int, input().split())
c = []
ans = 0
for i in range(h):
  c.append(list(input()))

for i in range(2 ** h - 1):
  c2 = []
  x = str(bin(i))[2:].zfill(h)
  for a in range(h):
    if x[a] == '0':
      c2.append(c[a])
    elif x[a] == '1':
      c2.append(['*'] * w)
  black = list(itertools.chain.from_iterable(c2)).count('#')
  for j in range(2 ** w - 1):
    black2 = black
    y = str(bin(j))[2:].zfill(w)
    for b in range(w):
      if y[b] == '1':
        for a in range(h):
          if c2[a][b] == '#':
            black2 -= 1
    if black2 == k:
      ans += 1
print(ans)
