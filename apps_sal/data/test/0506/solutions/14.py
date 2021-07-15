def main():
	a, b = list(map(int, input().split()))
	count = 0
	while a % b != 0 :
		count += (a//b)
		
		a = a % b
		if a < b:
			a, b = b, a
	count += a // b
	print(count )

def __starting_point():
	main()
		



__starting_point()
