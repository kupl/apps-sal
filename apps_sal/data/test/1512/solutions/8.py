n = int(input())
dct = {}
for i in range(1,n+1):
	dct[i] = 0
max1 = 0
max2 = 0
for i in list(map(int,input().split())):
	if i < max1:
		if i > max2:
			dct[max1] += 1
			max2 = i
	else:
		dct[i] -= 1
		max1,max2 = i,max1
m = -100
for i in dct:
	if dct[i] > m:
		m = dct[i]
		ans = i
print(ans)


