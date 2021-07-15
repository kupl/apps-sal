t = int(input())

for _ in range(t):
	n, k = list(map(int, input().split()))

	count = 0

	while n:
		if n%k==0:
			n //=k
			count += 1
		else:
			mod = n%k
			n -= mod
			count += mod

	print(count)


