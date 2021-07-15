X,Y=sorted(list(map(int,input().split())))
#移動方法を(i+1,j),(i,j+1)となるようにどうにかする
if (X-abs(Y-X))%3!=0 or X*2<Y:
  print((0))
  return
n=(X-abs(Y-X))//3
X=n+abs(Y-X)
Y=n

  
mod=10**9+7
a=1
for i in range(1,X+Y+1):
  a*=i
  a%=mod
b=1
for i in range(1,X+1):
  b*=i
  b%=mod
c=1
for i in range(1,Y+1):
  c*=i
  c%=mod

print((a*pow(b,-1,mod)*pow(c,-1,mod)%mod))

