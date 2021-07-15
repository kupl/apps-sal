import math
A,B,H,M=map(int,input().split())
x=2*math.pi*abs(H/12+M/60/12-M/60)
ans=pow(A*A+B*B-2*A*B*math.cos(x),1/2)
print(ans)
