x,a,b=map(int,input().split())

if b-a<=0:
  print('delicious')
  
elif 0<b-a<=x:
  print('safe')
  
else:
  print('dangerous')
