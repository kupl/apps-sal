n,k = map(int,input().split())
A = list(map(int,input().split()))
A = [0]+A;
x = 0
prev = [0 for i in range(n+1)]
sm = [0 for i in range(n+1)]
for i in range(1,n+1):
	prev[i] = x
	if A[i]>1:
		x = i
	sm[i] = A[i]+sm[i-1]
lim = int(2*(10**18))
ans = 0
for i in range(1,n+1):
	p = 1
	j = i
	while j:
		if lim//A[j]>p:
			s = sm[i]-sm[j-1]
			p *= A[j]
			sx = s+j-1-prev[j]
			if p%k == 0 and p>=k*s and p<=k*sx:
				ans += 1
		else:
			break
		j = prev[j]
print(ans)
