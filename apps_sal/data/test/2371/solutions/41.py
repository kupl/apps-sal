N, Z, W = map(int, input().split())
A = list(map(int, input().split()))
print(max(abs(A[N - 1] - A[N - 2]), abs(A[N - 1] - W)))
