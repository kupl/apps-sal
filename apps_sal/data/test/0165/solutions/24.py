tr = list(map(int, input().split()))
k = 0

tr.sort()

for i in range(2):
	if (tr[2] - 1) > tr[i]:
		 k += ((tr[2] - 1) - tr[i])

print(k)
