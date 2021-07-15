from itertools import groupby
R = lambda:map(int, input().split())
n, k = R()
a = list(R())
b = sorted(a[i] - k * i for i in range(1, n))
c = [(len(list(g[1])), g[0]) for g in groupby(b) if g[0] > 0]
if len(c) > 0:
  m = max(x for x, y in c)
  c = [x for x in c if x[0] == m]
else:
  c = [(0, a[0])]
d = 0
for i in range(len(c)):
  if c[i][1] == a[0]:
    d = i
    print(n - c[d][0] - 1)
    break
else:
  print(n - c[d][0])
for i in range(n):
  ai = c[d][1] + k * i
  if ai > a[i]:
    print("+ {} {}".format(i + 1, ai - a[i]))
  elif ai < a[i]:
    print("- {} {}".format(i + 1, a[i] - ai))
