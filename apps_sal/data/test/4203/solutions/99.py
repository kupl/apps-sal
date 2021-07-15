S = list(input())
stl = len(S) - 2
countOfC = 0


if S[0] != 'A':
  print('WA')
  return

for i in range(1, len(S)):
  if S[i].isupper():
    if i >= 2 and i <= stl and  S[i] == 'C':
      countOfC += 1
    else:
      print('WA')
      return

if countOfC == 1:
  print('AC')
else:
  print('WA')
