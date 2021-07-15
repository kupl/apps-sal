n = int(input())
i = 0
mx = 1
mn = 1000000000
nmx = 0
nmn = 0
a = list(map(int, input().split()))
for i in range(n):
	if a[i] > mx:
		mx = a[i]
		nmx = 1
	elif a[i] == mx:
		nmx += 1
	if a[i] < mn:
		mn = a[i]
		nmn = 1
	elif a[i] == mn:
		nmn += 1
if mx == mn:
	print('0', str(n*(n-1)//2))
else:
	print(str(mx - mn), str(nmn*nmx))

