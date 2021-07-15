N = input()
num = int(N)
Nls = list(N)
sum1 = sum([int(i) for i in Nls])
if num%sum1 == 0:
  print('Yes')
else:
  print('No')
