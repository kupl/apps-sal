n,k=list(map(int,input().split()))
l = list(map(int,input().split()))
s = sum(l)
req = k-0.5
if(s>=n*req):
	print(0)
	return
for i in range(1,100000):
	if((s+(k*i))>=(n+i)*req):
		print(i)
		return

