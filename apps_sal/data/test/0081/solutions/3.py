import sys
input = sys.stdin.readline

a,b=list(map(int,input().split()))

if a==b:
    print(0)
    return

if a>b:
    a,b=b,a

x=b-a

import math
xr=math.ceil(math.sqrt(x))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def lcm(x, y):
    return (x * y) // gcd(x, y)


LIST=[]
for i in range(1,xr+1):
    if x%i==0:
        LIST.append(i)
        LIST.append(x//i)

ANS=[]

for l in LIST:
    y=math.ceil(a/l)*l-a

    ANS.append([lcm(a+y,b+y),y])

    
print(min(ANS,key=lambda x:x[0])[1])


