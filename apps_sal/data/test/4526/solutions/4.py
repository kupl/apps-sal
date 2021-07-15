t = int(input())
spl = []

for i in range(8001):
	spl.append(0)

for i in range(t):
	n = int(input())
	arr = input().split(' ')

	for j in range(n):
		arr[j] = int(arr[j])

	for j in range(n):
		curr = arr[j]
		for k in range(j+1, n):
			curr += arr[k]
			if (curr > 8000):
				break
			spl[curr] = 1

	ans = 0

	for j in range(n):
		ans += (spl[arr[j]])

	for j in range(8001):
		spl[j] = 0

	print (ans)
