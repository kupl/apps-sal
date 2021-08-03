K, N = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * N
for i in range(N - 1):
    B[i] = A[i + 1] - A[i]
B[N - 1] = K - A[N - 1] + A[0]
print(K - max(B))
