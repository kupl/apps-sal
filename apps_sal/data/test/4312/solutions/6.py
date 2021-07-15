a, b, c, d = map(int, input().split())

ta = a
ao = c

while ta > 0 and ao > 0:
  ao = ao - b
  ta = ta - d
  
  if ao <= 0:
    print('Yes')  
  elif ta <= 0:
    print('No')
    return
