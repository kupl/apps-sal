n=int(input())
a=list(map(int,input().split()))
b=[0]*8
c=0
for x in a:
  if x<400:
    b[0]=1
  elif x<800:
    b[1]=1
  elif x<1200:
    b[2]=1
  elif x<1600:
    b[3]=1
  elif x<2000:
    b[4]=1
  elif x<2400:
    b[5]=1
  elif x<2800:
    b[6]=1
  elif x<3200:
    b[7]=1
  else:
    c+=1
x=b.count(1)
print(max(x,1),x+c)
