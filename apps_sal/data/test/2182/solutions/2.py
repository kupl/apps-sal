n = int(input())

for _ in range(n):
	s = input()

	if s.count('0') and sum(map(int, s)) % 3 == 0 and sum(int(c) % 2 == 0 for c in s) > 1:
		print("red")
	else:
		print("cyan")
