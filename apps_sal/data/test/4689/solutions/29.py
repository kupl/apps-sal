K, N = list(map(int, input().split()))
A = list(map(int, input().split()))
B = []

for j in range(N - 1):
    B.append(A[j + 1] - A[j])

C = A[0] + K - A[N - 1]
B.append(C)
B.sort()
print((K - B[N - 1]))
