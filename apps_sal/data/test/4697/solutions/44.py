n,m = map(int,input().split())
if n*2 <= m:
  m += n*2
  print(m//4)
else:
  print(m//2)
