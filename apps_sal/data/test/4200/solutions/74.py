N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

A = sorted(A, reverse=True)
S = sum(A)
ans = "No"
for i in range(M):
    if A[i] >= S / (4 * M):
        ans = "Yes"
    else:
        ans = "No"
        break
print(ans)
