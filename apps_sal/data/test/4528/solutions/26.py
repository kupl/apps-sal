N = int(input())


for _ in range(N):
	h, m = [int(x) for x in input().split()]

	print(24*60- (h*60+m))
