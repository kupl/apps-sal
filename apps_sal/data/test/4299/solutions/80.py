N = int(input())
F = N%10
if F in (2,4,5,7,9):
  print('hon')
elif F in (0,1,6,8):
  print('pon')
else:
  print('bon')
