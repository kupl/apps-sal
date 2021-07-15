import math
b=int(input())
k=1
c=0
x=math.floor(b**0.5)

while k<=x:
    if b%k==0:
        c+=2
    k+=1
if x*x==b:
    c-=1
print(c)
