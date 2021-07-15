import sys
pin=sys.stdin.readline

S=pin()[:-1]
Q=int(pin())
now=1
ans1=""
ans2=""
for i in range(Q):
  D=pin().split()
  T=0
  F=0
  C=""
  if len(D)==1:
    T=int(D[0])
  else:
    T=int(D[0])
    F=int(D[1])
    C=D[2]
  if T==1:
    now*=-1
  else:
    if F==1:
      if now==1:
        ans1=C+ans1
      else:
        ans2=ans2+C
    else:
      if now==1:
        ans2=ans2+C
      else:
        ans1=C+ans1
if now==1:
  print((ans1+S+ans2))
else:
  print((ans2[::-1]+S[::-1]+ans1[::-1]))


