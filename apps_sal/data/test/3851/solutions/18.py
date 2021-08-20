import sys
import math
'def solve(num,dis,a,b,k):\n    start=a\n    nex=(a+num)%k\n    if nex%k==b:\n        return dis//num\n    if (k-nex%k)==b:\n        return dis//num\n    start=dis-a\n    nex=(start+num)%dis\n    if nex%k==b:\n        return dis//num\n    if (k-nex%k)==b:\n        return dis//num\n    return -1'
(n, k) = list(map(int, sys.stdin.readline().split()))
(a, b) = list(map(int, sys.stdin.readline().split()))
factors = []
dis = n * k
"for i in range(1,int(math.sqrt(dis))+1):\n    if dis%i==0:\n        factors.append(i)\n        factors.append(dis//i)\n#print(factors,'factors')\nm=len(factors)\nnax,nin=-1,1e12+1\nfor i in range(m):\n    x=solve(factors[i],dis,a,b,k)\n    if x!=-1:\n        nax=max(nax,x)\n        nin=min(nin,x)"
start = a
(nax, nin) = (-1, 1000000000000.0 + 1)
for i in range(n):
    b1 = k * i + b
    if b1 > a:
        l = b1 - a
    else:
        l = dis - (a - b1)
    if l != 0:
        lcm = dis * l // math.gcd(dis, l)
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
        lcm = dis * l // math.gcd(dis, l)
        nax = max(nax, lcm // l)
        nin = min(nin, lcm // l)
print(nin, nax)
