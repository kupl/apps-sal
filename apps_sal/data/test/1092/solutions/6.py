M,N = 1000000007, 2000
f = [1]*N
for i in range(1,N):
	f[i] = f[i-1]*i%M

n,m = list(map(int,input().split()))
ar = sorted(map(int,input().split()))
br = []
for i in range(1,m):
	d = ar[i]-ar[i-1]-1
	if d>0:
		br.append(d)
res = pow(2,sum(br)-len(br),M)*f[n-m]%M
br = [ar[0]-1]+br+[n-ar[-1]]
for b in br:
	res = res*pow(f[b],M-2,M)%M
print(res)

