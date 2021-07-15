x, y = map(int,input().split(" "))

res = []
c = 'A'
while x * y > 1:
   k = min(x // y, x - 1)
   if k > 0:
      res.append('{}{}'.format(k, c))
   x, y = y, x - k*y
   c = 'A' if c == 'B' else 'B'

if x == 0 or y == 0:
   print('Impossible')
else:
   print(''.join(res))
