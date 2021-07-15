r,d,x2000 = map(int,input().split())

a = x2000

for x in range(10):
  a = r * a - d
  print(a)
