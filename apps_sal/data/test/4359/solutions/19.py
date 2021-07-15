a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=[a,b,c,d,e]
data=[0]*5
for i in range(5):
  if f[i]%10==0:
    continue
  else:
    data[i]=10-f[i]%10
print(a+data[0]+b+data[1]+c+data[2]+d+data[3]+e+data[4]-max(data))
