import sys
import math
'''def solve(num,dis,a,b,k):
    start=a
    nex=(a+num)%k
    if nex%k==b:
        return dis//num
    if (k-nex%k)==b:
        return dis//num
    start=dis-a
    nex=(start+num)%dis
    if nex%k==b:
        return dis//num
    if (k-nex%k)==b:
        return dis//num
    return -1'''
n, k = list(map(int, sys.stdin.readline().split()))
a, b = list(map(int, sys.stdin.readline().split()))
factors = []
dis = n * k
'''for i in range(1,int(math.sqrt(dis))+1):
    if dis%i==0:
        factors.append(i)
        factors.append(dis//i)
#print(factors,'factors')
m=len(factors)
nax,nin=-1,1e12+1
for i in range(m):
    x=solve(factors[i],dis,a,b,k)
    if x!=-1:
        nax=max(nax,x)
        nin=min(nin,x)'''
start = a
nax, nin = -1, 1e12 + 1
for i in range(n):
    b1 = k * i + b
    if b1 > a:
        l = b1 - a
    else:
        l = dis - (a - b1)
    if l != 0:
        lcm = (dis * l) // (math.gcd(dis, l))
        nax = max(nax, lcm // l)
        nin = min(nin, lcm // l)
st = k - a
for i in range(n):
    b1 = k * i + b
    if b1 > st:
        l = b1 - st
    else:
        l = dis - (st - b1)
    if l != 0:
        lcm = (dis * l) // (math.gcd(dis, l))
        nax = max(nax, lcm // l)
        nin = min(nin, lcm // l)
print(nin, nax)
