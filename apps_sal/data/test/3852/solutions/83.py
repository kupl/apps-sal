n,*a=map(int,open(0).read().split())
ans=[str(2*n-1)]
if max(a)>-min(a):
	i=a.index(max(a))
	for k in range(n):
		ans.append("{} {}".format(i+1,k+1))
	for k in range(n-1):
		ans.append("{} {}".format(k+1,k+2))
else:
	i=a.index(min(a))
	for k in range(n):
		ans.append("{} {}".format(i+1,k+1))
	for k in range(n-1):
		ans.append("{} {}".format(n-k,n-k-1))
print("\n".join(ans))
