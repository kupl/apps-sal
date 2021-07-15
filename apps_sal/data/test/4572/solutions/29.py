d = {}
for s in input():
  if s in d:
    d[s] += 1
  else:
    d[s] = 1

for a in 'abcdefghijklmnopqrstuvwxyz':
  if a not in d:
    print(a)
    return

print('None')
