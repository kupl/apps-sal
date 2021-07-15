n, k = list(map(int, input().split()))
powers = list(map(int, input().split()))[:n]

if k >= n - 1:
	print(max(powers))
else:
	wins = 0
	index = 0
	while True:
		A = index % n
		B = (index + 1) % n
		winner_power = -1
		if powers[A] < powers[B]:
			winner_power = powers[B]
			wins = 1
		else:
			winner_power = powers[A]
			powers[A], powers[B] = powers[B], powers[A]
			wins += 1
		index = B

		if wins >= k:
			print(winner_power)
			break

