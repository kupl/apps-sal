# AtCoder Beginner Contest 131
# C - Anti-Division
import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

A,B,C,D=list(map(int,input().split()))
bc=B//C
ac=(A-1)//C
cnum=bc-ac

bd=B//D
ad=(A-1)//D
dnum=bd-ad


lcmcd=lcm(C,D)
blcmcd=B//lcmcd
alcmcd=(A-1)//lcmcd
lcmcdnum=blcmcd-alcmcd


print((B-A-cnum-dnum+lcmcdnum+1))

