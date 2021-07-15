from math import gcd
n=int(input())
a=list(map(int,input().split()))
ma=max(a)
y=0
z=0
for i in a:
    z=gcd(z,ma-i)
for i in a:
    y+=(ma-i)//z
print(y,z)
    

