n=int(input())
t=input()
if t=='1':
  print(20000000000)
elif n%3==0:
  if t=='110'*(n//3):
    print(10000000000-n//3+1)
  elif t=='101'*(n//3) or t=='011'*(n//3):
    print(10000000000-n//3)
  else:
    print(0)
elif n%3==1:
  if t+'10'=='110'*(n//3+1) or '1'+t+'0'=='110'*(n//3+1) or '11'+t=='110'*(n//3+1):
    print(10000000000-n//3)
  else:
    print(0)
else:
  if t+'0'=='110'*(n//3+1) or '1'+t=='110'*(n//3+1):
    print(10000000000-n//3)
  elif '11'+t+'10'=='110'*(n//3+2):
    print(10000000000-n//3-1)
  else:
    print(0)
