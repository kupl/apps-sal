S = str(input())

S = S.replace('dream', '#')
S = S.replace('erase', '.')
S = S.replace('#er', '')
S = S.replace('.r', '')
S = S.replace('#', '')
S = S.replace('.', '')

if len(S) == 0:
  print('YES')
else:
  print('NO')

