import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
	n = int(sys.stdin.readline().strip())

	two, three = 0, 0
	while n%2 == 0:
		n //= 2
		two += 1
	while n%3 == 0:
		n //= 3
		three += 1

	if n > 1 or two > three:
		print(-1)
		continue

	else:
		print(three-two + three)

