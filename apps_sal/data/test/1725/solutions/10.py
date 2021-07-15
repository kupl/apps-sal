n,m,d = map(int,input().split())
array = []
for i in range(n):
	array.extend(map(int,input().split()))
array.sort()
mid = int(n*m/2)
ans = 0
notpossible = False
for i in range(n*m):
	if array[mid] > array[i]:
		diff = array[mid] - array[i]
		if diff%d != 0:
			notpossible = True
			break
		ans += int(diff/d)
	elif array[mid] < array[i]:
		diff = array[i] - array[mid]
		if diff%d != 0:
			notpossible = True
			break
		ans += int(diff/d)
if notpossible:
	print("-1")
else:
	print(ans)
