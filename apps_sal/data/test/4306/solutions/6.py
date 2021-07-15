A,B,C,D=map(int,input().split())
if A<=C:
  if D>=B:
    t=B-C
  else:
    t=D-C
else:
  if D>=B:
    t=B-A
  else:
    t=D-A
if t<=0:
  print(0)
else:
  print(t)
