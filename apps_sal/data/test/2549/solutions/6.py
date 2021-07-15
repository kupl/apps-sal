import sys,bisect
r=lambda:map(int,sys.stdin.readline().split())
M=998244353
def f(b):return pow(b,M-2,M)
n,m=r()
d=sorted(r())
p=[0]
for v in d:p+=[p[-1]+v]
o=[0]*m
for _ in range(m):
 a,b=r();i=bisect.bisect_left(d,b);v=n-i
 if a<=v:o[_]=(p[i]*a*f(v+v*v)-p[-1]*(a*f(v)-1))%M
print('\n'.join(map(str,o)))
