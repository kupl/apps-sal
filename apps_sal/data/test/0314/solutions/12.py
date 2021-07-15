def main():
	n, k = list(map(int, input().split()))
	candies = list(map(int, input().split()))

	rest = 0
	given = 0
	for i in range(n):
		rest += candies[i]
		if rest >= 8:
			given += 8
			rest -= 8
		else:
			given += rest
			rest = 0

		if given >= k:
			print(i + 1)
			break

		if i == n - 1:
			print(-1)

def __starting_point():
	main()
__starting_point()
