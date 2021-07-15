def L():
	return list(map(int, input().split()))

N = int(input())
A = L()
B = L()
C = L()
O = 0

for i in range(N):
	ai = A[i] - 1
	O += B[ai]
	if i > 0 and A[i] == A[i - 1] + 1:
		O += C[ai - 1]

print(O)
