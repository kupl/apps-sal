N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

B = [0] * N
for i in range(N):
    B[A[i] - 1] += 1

B.sort()

print((sum(B[0:N - K])))
