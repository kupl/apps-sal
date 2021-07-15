q = int(input())
for ifwfwe in range(q):
	n = int(input())
	i = 1
	odp = [0]
	while i*i <= n:
		odp.append(i)
		i += 1
	while i > 0:
		if n // i > odp[-1]:
			odp.append(n//i)
		i -= 1
	print(len(odp))
	print(*odp)
