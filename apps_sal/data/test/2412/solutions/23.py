t = int(input())
for i in range(t):
  n = int(input())
  s = input()
  st = False
  for i in range(n-1, -1, -1):
    if s[i]=='8' and n-i>=11:
      st = True
      break
  
  if st:
    print('YES')
  else:
    print('NO')
