n,k = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
l = max(a)-1
r = 100000000001

def check(s):
	count = 0
	l = 0
	r = n-1
	while l<=r:
		if l!=r and a[l]+a[r]<=s:
			count +=1
			l+=1
			r-=1
		else:
			r-=1
			count +=1
	if count <= k:
		return True
	else:
		return False

while (r-l>1):
	m = (r+l+1)//2
	#print(l,m,r)
	if check(m):
		r = m
	else:
		l = m
	
print(r)

