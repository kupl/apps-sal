n = input()
c = 2
s = 'YES'
for i in n:
  if i != '1' and i != '4':
    s = 'NO'
    break
  elif i == '4':
    c += 1
    if c > 2: 
      s = 'NO'
      break
  else: c = 0
print (s)

