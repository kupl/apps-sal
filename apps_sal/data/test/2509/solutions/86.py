n, k =map(int, input().split())
cnt=0

if k==0:
	print(n**2)
	return

for b in range(k+1,n+1):
	p,r=divmod(n,b)
	cnt+=p*(b-k)+max(0,r-k+1)
print(cnt)
