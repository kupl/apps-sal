t = int(input())
for _ in range(t):
	x = input()
	y = input()
	i = 1
	while y[-i] == "0":
		i += 1
	j = 0
	while x[-i-j] == "0":
		j += 1
	print(j)
