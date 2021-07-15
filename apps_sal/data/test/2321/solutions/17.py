t=int(input())
while t:
	t-=1
	n=int(input())
	s=input()
	l=0
	while l<n and s[l]!='>':
		l+=1
	r=n-1
	while r>=0 and s[r]!='<':
		r-=1
	print(min(min(l,n-1-r),n-1))
