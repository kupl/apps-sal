n=int(input())
li=list(map(int,input().split()))
b=max(li)
c=[]
n1=0
for i in li:
    if i!=b:
        c.append(b-i)
        n1+=1
import math
if n1==0:
    print(0,0)
else:
    a1=c[0]
    for i in c:
        a1=math.gcd(i,a1)
print(sum(c)//a1,a1)
    

