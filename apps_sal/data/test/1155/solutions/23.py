n,m = [int(i) for i in input().split()]
k = []
for i in range(n):
	a,b = [int(i) for i in input().split()]
	k.append(a*m/b)
print(min(k))

