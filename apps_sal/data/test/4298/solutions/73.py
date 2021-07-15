n,d = map(int,input().split())

eye = 2 * d +1

if n % eye == 0:
  print(n//eye)
  
else:
  print(n//eye +1)
