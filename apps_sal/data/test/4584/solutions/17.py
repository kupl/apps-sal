N = int(input())
A = list(map(int, input().split()))
A_count = [0] * N
for i in range(N - 1):
    A_count[A[i - 1] - 1] += 1
for i in range(N):
    print(A_count[i])
