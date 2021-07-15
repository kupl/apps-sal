import math

r,n=map(int,input().split())

if n-r>=5:
	print(0)
else:
	ans=1
	for i in range(r+1,n+1):
		ans*=i
	print(ans%10)
