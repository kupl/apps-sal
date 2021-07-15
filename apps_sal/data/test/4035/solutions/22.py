import math
A,B=map(int,input().split())
c=max(math.ceil(A/0.08),B*10)
d=min(int((A+1)/0.08),B*10+10)
print([-1,c][c<d])
