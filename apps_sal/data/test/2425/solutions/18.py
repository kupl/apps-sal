q = int(input())
A = [1] * 26
for i in range(1, 26):
	for j in range(2, int((2 ** i - 1) ** 0.5) + 1):
		if (2 ** i - 1) % j == 0:
			A[i] = (2 ** i - 1) // j
			break
for i in range(q):
	n = int(input())
	s = bin(n)[2:]
	if s != '1' * len(s):
		print(2 ** len(s) - 1)
	else:
		print(A[len(s)])
