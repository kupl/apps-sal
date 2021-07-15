def solve(x):
	total = 0
	total += (x//2)
	return(total)

t = int(input())
for _ in range(t):
	x = int(input())
	print(solve(x))
