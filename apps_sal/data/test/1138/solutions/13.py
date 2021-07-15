s = input()
if len(s)%2==1: print('-1')
else:
  L = s.count('L')
  R = s.count('R')
  U = s.count('U')
  D = s.count('D')
  print(int(abs(L-R)/2+abs(U-D)/2))
