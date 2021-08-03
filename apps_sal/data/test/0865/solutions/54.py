import numpy as np
N, T = map(int, input().split())
A, B = np.array([list(map(int, input().split())) for _ in range(N)]).T
dp1 = np.array([[0] * T for _ in range(N + 1)])
rev_A, rev_B = A[::-1], B[::-1]
dp2 = np.array([[0] * T for _ in range(N + 1)])


for i in range(1, N + 1):
    a = A[i - 1]
    rev_a = rev_A[i - 1]
    b = B[i - 1]
    rev_b = rev_B[i - 1]

    dp1[i, :a] = dp1[i - 1, :a]
    dp2[i, :rev_a] = dp2[i - 1, :rev_a]
    dp1[i, a:] = np.fmax(dp1[i - 1, a:], dp1[i - 1, :-a] + b)
    dp2[i, rev_a:] = np.fmax(dp2[i - 1, rev_a:], dp2[i - 1, :-rev_a] + rev_b)


lis = [0] * N
for i in range(1, N + 1):
    lis[i - 1] = (np.max(dp1[i - 1] + dp2[N - i][::-1]) + B[i - 1])


print(max(lis))
