h, a = map(int, input().split())

if h%a != 0:
  print(h//a+1)
else:
  print(h//a)
