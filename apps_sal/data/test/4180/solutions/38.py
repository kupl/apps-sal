N = int(input())
if N % 1000 == 0:
  print(0)
else:
  while N > 1000:
    N -= 1000
  print(1000-N)
