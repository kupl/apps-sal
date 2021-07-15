from math import gcd
from functools import reduce

n,m=map(int,input().split())
lst=list(map(lambda x : int(x)//2,input().split()))
divi=0
x=lst[0]
while x%2==0:
    x//=2
    divi+=1

for i in range(1,n):
    divi2=0
    x=lst[i]
    while x%2==0:
        x//=2
        divi2+=1
    if divi!=divi2 :
        print(0)
        return

work=reduce(lambda x,y: x*y//gcd(x,y),lst)
print((m//work+1)//2)
