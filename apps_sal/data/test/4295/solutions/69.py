N, K = list(map(int, input().split()))

if N == 0:
	print(N)
else:
	div = N // K
	print((min(N - div * K, (div + 1) * K - N)))

