N = int(input())
if N % 2 != 0 or N < 10:
  print(0)
else:
  n = N // 2
  count5 = 0
  while n >= 5:
    n = n // 5
    count5 += n
  print(count5)
