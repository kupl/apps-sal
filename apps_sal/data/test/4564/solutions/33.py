S = input()
T = sorted(S)
U = set(T)
U = sorted(U)
if T == U:
  print('yes')
else:
  print('no')

