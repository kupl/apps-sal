n = int(input())

s = sum(list(map(int, str(n))))
if n % s == 0:
  print('Yes')
else:
  print('No')
