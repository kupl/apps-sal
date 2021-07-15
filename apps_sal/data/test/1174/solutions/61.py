def main():
	N, M = [int(x) for x in input().split(" ")]
	A = [int(a) for a in input().split(" ")]
	D = []
	for i in range(len(A)):
		tmp = A[i]
		while tmp > 0:
			half = int(tmp / 2)
			D.append(tmp - half)
			tmp = half
	D.sort(reverse=True)
	print(sum(A) - sum(D[:M]))

main()
