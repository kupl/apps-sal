n = int(input())
tall = []
for i in range(n):
	a,b = map(int,input().split())
	tall.append([a,b])
check = True
now = max(tall[0])
for i in range(1,n):
	if tall[i][0] <= now and tall[i][1] <= now:
		now = max(tall[i])
	elif tall[i][0] <= now:
		now = tall[i][0]
	elif tall[i][1] <= now:
		now = tall[i][1]
	else:
		check = False
if check:
	print('YES')
else:
	print('NO')
