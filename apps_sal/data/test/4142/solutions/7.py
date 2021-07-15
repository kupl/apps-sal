s = input()
for i, si in enumerate(s):
  if si in ['U', 'D']:
    continue
  if i % 2 == 1 and si == 'L':
    continue
  if i % 2 == 0 and si == 'R':
    continue
  print('No')
  return
print('Yes')

