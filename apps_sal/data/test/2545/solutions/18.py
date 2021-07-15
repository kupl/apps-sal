t=int(input())
for i in range(t):
	a,b=list(map(int,input().split()))
	if a<b:
		a,b=b,a
	p=a-b
	a-=p*2
	b-=p
	if a%3==0 and b>=0:
		print("YES")
	else:
		print("NO")

