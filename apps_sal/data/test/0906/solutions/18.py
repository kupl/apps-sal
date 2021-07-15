mod=1000000007
def sqr(n):return n*n%mod
def pow(a,n):
	if n==0:return 1
	if n%2==1:return sqr(pow(a,n>>1))*a%mod
	return sqr(pow(a,n>>1))

n,m,k=list(map(int,input().split()))
if (n+m)%2==1 and k==-1:
	print(0)
	return
print(pow(2,(n-1)*(m-1)))

