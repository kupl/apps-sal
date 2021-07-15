n = int(input())
ss = sorted([int(input()) for i in range(n)])
tss = sum(ss) # total ss
if tss % 10 != 0:
  print(tss)
else:
  for s in ss:
    x = tss - s
    if  x % 10 != 0:
      print(x)
      return
  print(0)
