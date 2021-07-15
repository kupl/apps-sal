import math

w,m=map(int,input().split())
while m>0:
	if m%w==1:
		m-=1
		m/=w
	elif m%w==w-1:
		m+=1
		m/=w
	elif m%w==0:
		m/=w
	else:
		print("NO")
		return
print("YES")
