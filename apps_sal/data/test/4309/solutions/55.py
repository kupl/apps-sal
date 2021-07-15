N = int(input())
if N < 111:
  print(111)
else:
  for i in range(1,10):
    if N <= 111*i:
      ans = 111*i
      break
  print(ans)
