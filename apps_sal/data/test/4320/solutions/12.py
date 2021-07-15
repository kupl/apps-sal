for _ in range(1, int(input()) + 1):
	n = int(input())
	for i in range(2, 36):
		if( n % (2**i - 1) == 0):
			print(n//(2**i - 1))
			break
