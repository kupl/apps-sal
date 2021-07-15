n, k = list(map(int, input().split(' ')))
x = list(map(int, input().split(' ')))

m = 0
i = 0
while i != len(x)-1:
	if (x[i+1] - x[i]) == k:
		m += 1
		i += 1
	elif (x[i+1] - x[i]) < k:
		for j in range(i + 1, len(x)):
			if (x[j] - x[i]) > k:
				break
		else:
			j += 1
		i = j-1
		m += 1
	else:
		m = -1
		i = len(x)-1

print(m)

