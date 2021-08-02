N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for i in range(N):
    if A[i] < B[i]:
        res += min(A[i + 1] + A[i], B[i])
        A[i + 1] = max(A[i + 1] + A[i] - B[i], 0)
    else:
        res += B[i]

print(res)
