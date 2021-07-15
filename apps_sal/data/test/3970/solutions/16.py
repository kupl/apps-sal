def bSearch(x,li):
	l=0
	h=len(li)
	while(l<=h):
		m=(l+h)//2
		if(li[m]==x):
			return m
		elif(li[m]>x):
			h=m-1
		else:
			l=m+1
	return -1
n,k=list(map(int,input().split()))
li=list(map(int,input().split()))
li.sort()
s=set()
for i in range(n):
	if(li[i]%k==0):
		z = bSearch(li[i]//k,li)
		if(z!=-1):
			if li[z] not in s:
				s.add(li[i])
		else:
			s.add(li[i])
	else:
		s.add(li[i])
print(len(s))
		

