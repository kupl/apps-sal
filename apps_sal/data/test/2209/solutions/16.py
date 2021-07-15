def mycmp(a,b):
	if (a[0]*b[1]>b[0]*a[1]):
		return -1
	return 1

n=int(input())
a=[]
ans=0
for i in range(1,n+1):
	str=input()
	totlen=len(str)
	s=h=0
	for j in range(0,totlen):
		if (str[j]=='s'):
			s=s+1
		else:
			h=h+1
			ans=ans+s
	tmp=0
	if (h==0):
		tmp=1e18
	else:
		tmp=s/h
	a.append((int(s),int(h),tmp))
	#print(s,h)
a.sort(key=lambda x:x[2],reverse=True)
sum=0
for i in range(0,len(a)):
	ans=ans+sum*a[i][1]
	sum=sum+a[i][0]
print(ans)

