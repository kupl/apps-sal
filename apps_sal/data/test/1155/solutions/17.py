n,m=map(int, input().split())
cost=10**7
for i in range(n):
	a,b=map(int, input().split())
	if (a/b)<cost:
		cost=a/b
print(cost*m)
