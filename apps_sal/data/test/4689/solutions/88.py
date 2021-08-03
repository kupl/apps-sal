K, N = map(int, input().split())
A = [int(i) for i in input().split()]
A.append(A[0] + K)
max = 0
for i in range(N):
    if max <= (A[i + 1] - A[i]):
        max = A[i + 1] - A[i]

print(K - max)
