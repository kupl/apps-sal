def sum(a,b):
	if a>b:
		return sum(b,a)
	n=b-a+1
	return (a+b)*n//2

[n,h]=[int(x) for x in input().split()]
l=0
r=n
while l+1<r:
	m=(l+r)//2
	mx=0
	if m<h:
		mx=sum(1,m)
	else:
		if m%2==h%2:
			hm=(h+m)//2
			mx=sum(h,hm)+sum(1,hm-1)
		else:
			hm=(h+m)//2
			mx=sum(h,hm)+sum(1,hm)
	if mx>=n:
		r=m
	else:
		l=m
print(r)
