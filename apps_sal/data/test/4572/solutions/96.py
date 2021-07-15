S = list(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'

for a in alpha:
  if S.count(a) == 0:
    print(a)
    break
else:
  print("None")
