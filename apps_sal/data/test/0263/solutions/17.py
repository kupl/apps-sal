import math
n=int(input())
m=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

x=max(a)
y=min(a)
op=((sum(a)+m)/n)
# print(op)
if(op!=int(op)):
    op=op+1
print(max(x,int(op)),x+m)

