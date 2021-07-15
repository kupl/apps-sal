def main():
	N = int(input())
	A = [int(a) for a in input().split(" ")]
	exA = A * 2
	S = sum(A)
	D = [sum(A[1::2]), sum(A[2::2])]
	for i in range(2, N):
		D.append(D[-2] - exA[i - 1] + exA[i + N - 2])
	print((" ".join([str(S - 2 * d) for d in D])))

main()

