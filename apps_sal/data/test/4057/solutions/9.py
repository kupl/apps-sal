n = int(input().strip())
a = [int(x) for x in input().strip().split(' ')]
v = [0]*101
for i in range(n):
	v[a[i]]+=1
print(max(v))
