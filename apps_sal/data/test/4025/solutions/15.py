a, b, c = list(map(int, input().split()))

a1, b1, c1 = a, b, c

k = min(a // 3, b // 2, c // 2)


a -= 3 * k
b -= 2 * k
c -= 2 * k

aa = [1, 2, 3, 1, 3, 2, 1]

aa += aa[:]

mx = 0
ind = 1

for i in range(7):
	var = [0, a, b, c]
	kol = 0
	
	for j in range(i, 7 + 7):
		if var[aa[j]] == 0:
			break
		var[aa[j]] -= 1
		kol += 1
	
	if kol > mx:
		mx = kol
		ind = i + 1


print(k * 7 + mx)

