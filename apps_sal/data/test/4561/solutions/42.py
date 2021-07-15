x, a, b=list(map(int, input().split()))
if a>=b:
  print('delicious')
else:
  if b-a<x+1:
    print('safe')
  else:
    print('dangerous')

