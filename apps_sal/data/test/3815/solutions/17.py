import sys
try:
	fin = open('in')
except:
	fin = sys.stdin
input = fin.readline

mod=10**9+9
def f(x,y):
	ans=1
	while y:
		if y&1:ans=ans*x%mod
		x=x*x%mod
		y>>=1
	return ans
n,a,b,k=map(int,input().split())
s=[1 if c=='+' else -1 for c in input()]
#period k-1
pr=sum(s[i]*f(a,n-i)*f(b,i) for i in range(k))%mod
#ratio (b/a)^k
rt=f(b,k)*f(f(a,k),mod-2)%mod
terms=(n+1)//k
if rt==1:
	print(terms*pr%mod)
else:
	print(pr*(f(rt,terms)-1)*f(rt-1,mod-2)%mod)
