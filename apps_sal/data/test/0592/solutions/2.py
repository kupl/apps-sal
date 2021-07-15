import sys
n=int(input())

if n<=3:
    print(0)
    return

score=0
import math
def score(x):
    ANS=0
    xr=math.ceil(math.sqrt(x))

    LIST=[]
    for i in range(1,xr+3):
        if x%i==0:
            LIST.append(i)
            LIST.append(x//i)

    LIST=sorted(list(set(LIST)))

    for l in LIST[1:-1]:
        ANS+=x//l

    return ANS

ANS=0
for i in range(4,n+1):
    ANS+=score(i)

print(ANS*4)
    


