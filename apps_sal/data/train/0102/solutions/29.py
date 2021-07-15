for _ in range(int(input())):
	N = input()
	kolvo = (len(N) - 1) * 9
	for i in range(1, 10):
		kolvo += int(str(i) * len(N)) <= int(N)
	print(kolvo)

