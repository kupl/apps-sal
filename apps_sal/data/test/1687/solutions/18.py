n=int(input())
a=[int(x) for x in input().split()]
def gcd(a,b):
	a,b=max(a,b),min(a,b)
	while True:
		if a%b==0:
			return b
		b=a%b
		a=b
if n==1:
	print(a[0])
	return
ans=max(a)
for i in range(1,n):
	temp=gcd(a[i],a[i-1])
	if temp<=ans:
		ans=temp
	if ans==1:
		break
for i in a:
	if i%ans!=0:
		print(-1)
		return
if ans in a:
	print(ans)
else:
	print(-1)
