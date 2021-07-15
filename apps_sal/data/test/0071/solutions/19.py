n, m, k, x, y = tuple(map(int, input().split()))

maxq = minq = sergeiq = 0
if n == 1:
	maxq = k // m
	if k % m > 0:
		maxq +=1
		minq = maxq - 1
		if y <= k % m:
			sergeiq = maxq
		else:
			sergeiq = minq
	else:
		minq = maxq
		sergeiq = minq
elif n == 2:
	maxq = minq = sergeiq = k // (2*m)
	if k % (2*m) > 0:
		maxq += 1
		if x == 1 and y <= k % (2*m):
			sergeiq += 1
		elif x == 2 and k % (2*m) >= y + m:
			sergeiq += 1
elif k < n * m:
	maxq = 1
	minq = 0
	if k / m >= x:
		sergeiq = 1
	elif k / m <= x-1:
		sergeiq = 0
	elif k % m >= y:
		sergeiq = 1
	else:
		sergeiq = 0
elif k == n*m:
	maxq = 1
	minq = 1
	sergeiq = 1
else:
	maxq = 2*(k // (m * 2 * (n-1)))
	minq = k // (m * 2 * (n-1))
	if x == 1 or x == n:
		sergeiq = minq
	else:
		sergeiq = maxq
	remainder = k % (m * 2* (n-1))
	if remainder > 0:
		if remainder <= m:
			if x == 1 and y <= remainder:
				sergeiq += 1
		elif remainder <= m * n:
			maxq += 1
			if x <= remainder / m:
				sergeiq += 1
			elif x-1 < remainder / m and remainder % m >= y:
				sergeiq += 1
			if remainder == m*n:
				minq += 1
		else:
			maxq += 2
			sergeiq += 1
			minq += 1
			if x != 1 and x != n:
				if (remainder - (n*m)) / m >= n-x:
					sergeiq += 1
				elif (remainder - (n*m)) / m > n-x-1 and (remainder - (n*m)) % m >= y:
					sergeiq += 1
print(str(maxq) + ' ' + str(minq) + ' ' + str(sergeiq))


