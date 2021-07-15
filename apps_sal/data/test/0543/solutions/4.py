__author__ = 'Think'
def f(k):
	if k==0:
		return 0
	elif (k%2)==1:
		return 1
	else:
		return 2
n=int(input())
teams=[f(int(i)) for i in input().split()]
coupon=False
working=True
for i in teams:
	if coupon:
		if i==0:
			working=False
			break
		else:
			i-=1
	coupon=((i%2)==1)
if (not coupon) and working:
	print("YES")
else:
	print("NO")
