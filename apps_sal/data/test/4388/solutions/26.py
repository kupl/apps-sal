ret = ''
for a in input():
  if a == '1':
    ret += '9'
  elif a == '9':
    ret += '1'
  else:
    ret += a
print(ret)

