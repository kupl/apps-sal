n = int(input())
a = list(map(int,input().split()))

sum = 0
max = a[0]

for i in range(n):
	if(max > a[i]):
		sum += (max - a[i])
	else:
		max = a[i]
print(sum)
