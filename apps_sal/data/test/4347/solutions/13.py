def solve():
	n = int(input())
	n -= 2
	num = 2
	for i in range(1,n+2):
		num *= i
	num = num // (n+2)
	return num

#main
print(solve())
