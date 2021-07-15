n = int(input())
a = list(map(int,input().split()))
b = -1
for i in range(1,n):
	if a[i-1]>a[i]:
		b = i
		break
if b==-1:
	print(0)
else:
	c = a[b:]+a[:b]
	flag = 0
	for i in range(1,n):
		if c[i]<c[i-1]:
			flag = 1
			break
	if flag == 1:
		print(-1)
	else:
		print(n-b)




