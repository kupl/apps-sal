n,m = map(int, input().split(" "))
ks = [list(map(int, input().split(" "))) for i in range(m)]
p = list(map(int, input().split(" ")))
total = 0
for i in range(2 ** n):
  count = 0
  den = [0 for i in range(m+1)]
  for j in range(n):
    if i >> j & 1:
      for k in range(m):
        #print(i, j+1, ks[k][1:])
        if j+1 in ks[k][1:]:
          den[k+1] += 1
  #print(i, den)
  for j in range(m):
    if den[j+1] % 2 == p[j]:
      count += 1
  if count == m:
    total += 1
print(total)
