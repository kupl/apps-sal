n, m = map(int, input().split())
a1 = []
bn = []

for i in range(m):
  a, b = map(int, input().split())
  if a == 1:
    a1.append(b)
  elif b == n:
    bn.append(a)
la = len(a1)
lb = len(bn)
sa = set(a1)
sb = set(bn)
if len(sa | sb) < la + lb:
  print('POSSIBLE')
  return
print('IMPOSSIBLE')
