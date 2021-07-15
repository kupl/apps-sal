input()
x=list(map(int,input().split()))
r=10**10
for i in range(min(x),max(x)+1):
	s=0
	for j in x:
		s+=(i-j)**2
	r=min(r,s)
print(r)
