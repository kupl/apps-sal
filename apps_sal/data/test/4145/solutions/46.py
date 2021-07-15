x=int(input())
while True:
  flag=0
  for i in range(2,int(x**0.5)+2):
    if x%i==0:
      flag=1
      break
    else:
      continue
  if x==2:
    flag=0
  if flag==0:
    print(x)
    break
  else:
    x+=1
