import math
s = [int(input()) for i in range(5)]
k=int(input())
q=0
if abs(s[4]-s[0])<=k:
   q=1
if q==1:
   print('Yay!')
if q==0:
  print(':(')

