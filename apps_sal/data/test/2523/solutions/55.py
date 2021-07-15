w=input()
a=[(i+1)*(j=="0") for i,j in enumerate(w)]
b=[(i+1)*(j=="1") for i,j in enumerate(w)]
l=len(w)
ma=a[0];mb=b[0]
for t in range(1,l+1):
	ma=max(ma,a[t-1])
	mb=max(mb,b[t-1])
	m=min(ma,mb)
	if l-m<t:
		print(t-1)
		return
print(l)
