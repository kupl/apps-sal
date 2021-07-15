n,k = list(map(int,input().split()))
if 2*n<k*(k+1):
	print(-1)
	return
mx = 0

def ok(d):
	sm = k*(k-1)//2
	sm *= d
	if sm+k>n:
		return False
	if (n-sm>((k-1)*d)):
		return True
	else:
		return False

i = 1
while i*i<=n:
	if n%i==0:
		if ok(i): mx = max(mx,i)
		if ok(n//i): mx = max(mx,n//i)
	i+= 1
ans = ''
for i in range(1,k):
	ans += str(i*mx)+' '
ans += str(n-((k*(k-1))//2)*mx)
print(ans)

