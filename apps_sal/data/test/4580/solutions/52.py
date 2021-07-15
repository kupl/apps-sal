n=int(input())
a=list(map(int,input().split()))
b=[0]*9
for i in range(n):
  if a[i]<400:
    b[0]+=1
  elif a[i]<800:
    b[1]+=1
  elif a[i]<1200:
    b[2]+=1
  elif a[i]<1600:
    b[3]+=1
  elif a[i]<2000:
    b[4]+=1
  elif a[i]<2400:
    b[5]+=1
  elif a[i]<2800:
    b[6]+=1
  elif a[i]<3200:
    b[7]+=1
  else:
    b[8]+=1
    
min=8-b[:8].count(0)
max=min+b[8]

if min==0:
  min=1
print(min,max)
