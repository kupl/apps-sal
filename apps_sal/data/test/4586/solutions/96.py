a=input()
b=set(a[:-1]);c=set(a[1:])

if len(b)==1 or len(c)==1:
  print('Yes')
else:
  print('No')

