import math

N,X=list(map(int,input().split()))
x=list(map(int,input().split()))
D=abs(x[0]-X)
for i in range(1,N):
    D=math.gcd(D,abs(x[i]-X))
print(D)

