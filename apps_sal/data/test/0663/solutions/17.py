from math import sqrt as S
r,x,y,X,Y=list(map(int,input().split()))
D=(x-X)*(x-X)+(y-Y)*(y-Y)
d=S(D)
r*=2
k=d/r
j=int(k)
T=j*r
T=T*T
if T!=D:j+=1
print(j)

