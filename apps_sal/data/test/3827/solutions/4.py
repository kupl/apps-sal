x=input()
last=''
for i in x:
 if i==last: continue
 elif last=='' and i=='a':
  last='a'
 elif last=='a' and i=='b':
  last='b'
 elif last=='b' and i=='c':
  last='c'
 else:
  print('NO')
  return

if x.count('a') and x.count('b') and (x.count('a')==x.count('c') or x.count('b')==x.count('c')):
 print('YES')
else: print('NO')
