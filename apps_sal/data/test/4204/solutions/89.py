s = input()
k = int(input())
i = 0
while True:
  if s[i] == '1':
    if k <= i+1:
      print('1')
      break
    else:
      i += 1
  else:
    print(s[i])
    break
