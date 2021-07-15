for i in range(int(input())):
  s = input()
  l = len(s)-1
  if s[l] == 'o':
    print('FILIPINO')
  elif s[l] == 'u':
    print('JAPANESE')
  else:
    print('KOREAN')
