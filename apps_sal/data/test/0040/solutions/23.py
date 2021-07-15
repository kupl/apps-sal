n=int(input())
max=4127
T=True
for i in range(n):
	l,r=list(map(int,input().split()))
	if l==r:
		if max<l:
			T=False
		max=l
	else:
		print("rated")
		break
else:
	if T:
		print("maybe")
	else:
		print("unrated")

