import sys
input = sys.stdin.readline
(n, x) = list(map(int, input().split()))
A = list(map(int, input().split()))
DP0 = [0] * (n + 1)
DP1 = [0] * (n + 1)
DP2 = [0] * (n + 1)
for i in range(n):
    DP0[i] = max(DP0[i - 1] + A[i], A[i], 0)
    DP1[i] = max(DP0[i - 1] + A[i] * x, DP1[i - 1] + A[i] * x, DP0[i])
    DP2[i] = max(DP2[i - 1] + A[i], DP1[i - 1] + A[i], DP1[i])
print(max(DP2))
