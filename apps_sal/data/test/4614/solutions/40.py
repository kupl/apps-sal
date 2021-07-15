ls = list(map(int,input().split()))
if ls[1] != ls[2] and ls[2] == ls[0]:
  print((ls[1]))
if ls[0] != ls[1] and ls[1] == ls[2]:
  print((ls[0]))
if ls[2] != ls[1] and ls[1] == ls[0]:
  print((ls[2]))

