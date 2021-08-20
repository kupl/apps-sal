N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(N):
    cnt += min(A[i], B[i])
    if A[i] < B[i]:
        if A[i + 1] < B[i] - A[i]:
            cnt += A[i + 1]
            A[i + 1] = 0
        else:
            cnt += B[i] - A[i]
            A[i + 1] -= B[i] - A[i]
print(cnt)
