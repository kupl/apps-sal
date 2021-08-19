N = int(input())
(A, B, C) = [list(map(int, input().split())) for _ in range(3)]
ans = 0
for i in range(N - 1):
    if A[i + 1] == A[i] + 1:
        ans += C[A[i] - 1]
print(sum(B) + ans)
