a = input()
test = ''
for i in range(len(a)):
  if a[i] == '0':
    test += '0'
  elif a[i] == '1':
    test += '1'
  else:
    if len(a) == 0:
      pass
    else:
      test = test[:-1]
    
print(test)
