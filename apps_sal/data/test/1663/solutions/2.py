import sys
z=sys.stdin.readline
M=10**9+7
n=[*map(int,z().strip())]
l=len(n)
p=[0]
for i in range(l):p.append(p[-1]+n[i])
s=0
v=(l*l-l)//2
d=1
for i in range(1,l):
    r=p[l-i]*i+v*n[l-i]
    s=(s+r*d)%M
    d=(d*10)%M
    v-=l-i
print(s)
