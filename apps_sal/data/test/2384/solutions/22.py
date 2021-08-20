N = int(input())
A = list(map(int, input().split())) + [0]
(dp0, dp1, dp2) = ([0] * (N + 1), [0] * (N + 1), [0] * (N + 1))
dp0[0] = A[0]
dp1[1] = A[1]
dp2[2] = A[2]
for i in range(N - 3):
    dp0[i + 2] = 0 if i % 2 else dp0[i] + A[i + 2]
    dp1[i + 3] = max(dp0[i], dp1[i + 1]) + A[i + 3]
    dp2[i + 4] = max(dp0[i], dp1[i + 1], dp2[i + 2]) + A[i + 4]
if N % 2:
    print(max(dp0[N - 3], dp1[N - 2], dp2[N - 1]))
else:
    print(max(dp0[N - 2], dp1[N - 1]))
