N = int(input())
n = N % 10
if n in [2,4,5,7,9]:
  print('hon')#.format(N))
elif n in [0,1,6,8]:
  print('pon')#.format(N))
else:
  print('bon')#.format(N))
