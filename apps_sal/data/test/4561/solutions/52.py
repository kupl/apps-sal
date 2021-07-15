x,a,b=list(map(int, input().split()))


if -a+b <=0:
  print('delicious')
elif -a+b < x+1:
  print('safe')
else:
  print('dangerous')

