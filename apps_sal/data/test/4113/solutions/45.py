N = int(input())
out = 'No'
for x in range(N // 4 + 1):
	for y in range(N // 7 + 1):
		if 4 * x + 7 * y == N:
			out = 'Yes'
			break
print(out)

