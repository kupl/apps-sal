N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = sum(A)
for i in range(N):
    if A[i] >= B[i]:
        A[i] -= B[i]
    else:
        B[i] -= A[i]
        A[i] = 0
        A[i + 1] = max(A[i + 1] - B[i], 0)
ans -= sum(A)
print(ans)
