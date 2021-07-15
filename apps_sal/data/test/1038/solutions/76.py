def main():
	A, B = [int(n) for n in input().split(" ")]
	d = B - A
	if d == 0:
		print(A)
		return 0
	if d == 1:
		print(A ^ B)
		return 0
	begin = A + A % 2
	end = B + B % 2 - 1
	pair = int((end - begin + 1) / 2)
	print((A * (A % 2)) ^ pair % 2 ^ (B * (1 - B % 2)))

main()
