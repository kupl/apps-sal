for _ in range(int(input())):
	n, k = list(map(int, input().split()))
	A = list(map(int, input().split()))

	A.sort(reverse=True)
	if k == 0:
		print(max(A) - min(A))
	else:
		print(A[0] + sum(A[1:k+1]))

