N = int(input())
A = list(map(int, input().split()))
B = [0] * N
for i in range(0, N - 1):
    B[A[i] - 1] += 1

for i in range(N):
    print((B[i]))
