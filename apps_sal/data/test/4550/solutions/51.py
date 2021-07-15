A, B, C = [int(i) for i in input().split()]
x = max(A, B, C)
s = sum([A, B, C])
y = s - x

if x == y:
  print('Yes')
else:
  print('No')

