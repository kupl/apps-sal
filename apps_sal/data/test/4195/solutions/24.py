n,m = [int(x) for x in input().split()]
if m != 100:
  print((100**n) * m) 
else:
  print((100**n) * (m+1))
