(N, X) = map(int, input().split())
(*A,) = map(int, input().split())
B = [0] * N
for i in range(N):
    B[i] = A[i] if A[i] <= X else X
cnt = sum(A) - sum(B)
for i in range(N - 1):
    if X < B[i] + B[i + 1]:
        d = B[i] + B[i + 1] - X
        B[i + 1] -= d
        cnt += d
print(cnt)
