from collections import Counter
s=input()
c=Counter(s)
if c['x']>c['y']:
  print('x'*(c['x']-c['y']))
else:
  print('y'*(c['y']-c['x']))


