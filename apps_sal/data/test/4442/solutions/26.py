a, b = map(int, input().split())
aa = str(a)*b
bb = str(b)*a

aa = ''.join(aa)
bb = ''.join(bb)

if aa > bb:
  print(bb)
else:
  print(aa)
