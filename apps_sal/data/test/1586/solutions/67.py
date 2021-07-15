n = int(input())
cnt = 0
x = len(str(n))

if n % 2 == 1:
  print((0))
else:
  for i in range(1,26):
    cnt += n//((5**i)* 2)
  print(cnt)

