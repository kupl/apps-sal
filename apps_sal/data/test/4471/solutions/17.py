

for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))

	f=0

	for i in range(n):
		for j in range(i+1,n):
			if(abs(a[i]-a[j])&1):
				f=1
	if(f):
		print("NO")
	else:
		print("YES")
