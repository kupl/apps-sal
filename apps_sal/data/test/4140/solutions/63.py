a=input()
b=int(len(a))
c=0
d=0
if b%2==0:
  for i in range(b//2):
    if a[2*i]=="1":
      c=c+1
    if a[2*i+1]=="0":
      c=c+1
  for i in range(b//2):
    if a[2*i]=="0":
      d=d+1
    if a[2*i+1]=="1":
      d=d+1
  if c>d:
    print(d)
  else:
    print(c)
if b%2==1:
  for i in range(b//2):
    if a[2*i]=="1":
      c=c+1
    if a[2*i+1]=="0":
      c=c+1
  if a[-1]=="1":
    c=c+1
  for i in range(b//2):
    if a[2*i]=="0":
      d=d+1
    if a[2*i+1]=="1":
      d=d+1
  if a[-1]=="0":
    d=d+1
  if c>d:
    print(d)
  else:
    print(c)
