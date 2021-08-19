N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [0] * (N + 1)
cnt = 0
C[0] = A[0]
for i in range(1, N + 1):
    if C[i - 1] > B[i - 1]:
        C[i] = A[i]
        cnt += A[i - 1] + B[i - 1] - C[i - 1]
    elif C[i - 1] <= B[i - 1]:
        if A[i] - B[i - 1] + C[i - 1] >= 0:
            C[i] = A[i] - B[i - 1] + C[i - 1]
            cnt += A[i - 1]
        else:
            C[i] = 0
            cnt += A[i - 1]
if B[N - 1] - C[N - 1] > 0:
    ans = cnt + min(A[N], B[N - 1] - C[N - 1])
else:
    ans = cnt
print(ans)
