t = int(input())

for _ in range(t):
	a, b = map(int, input().split())
	diff = abs(a-b)
	fives = diff//5
	diff %= 5
	twos = diff//2
	diff %= 2
	ones = diff

	print(fives+twos+ones)
