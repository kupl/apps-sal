n = int(input())

a = list(map(int,input().strip().split(' ')))

d = a[1] - a[0]
fl = True
for i in range(2,n):
	cd = a[i] - a[i-1]
	if d != cd:
		fl = False
		break
	
if fl:
	print(a[n-1] + d)
else:
	print(a[n-1])

