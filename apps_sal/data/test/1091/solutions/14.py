n = int(input())
a = list(input().split())
mx = -1
mx2 = -1
pos = -1
for i in range(0, n):
	a[i] = int(a[i])
	if(a[i] > mx):
		mx2 = mx
		pos = i + 1
		mx = a[i]
	elif(a[i] > mx2):
		mx2 = a[i]
	i = i + 1
print(str(pos) + ' ' + str(mx2))
