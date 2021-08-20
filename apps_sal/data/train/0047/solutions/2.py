import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    (n, q) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    DP0 = [0] * n
    DP1 = [0] * n
    for i in range(n):
        DP0[i] = max(DP0[i - 1], DP1[i - 1] + A[i])
        DP1[i] = max(DP1[i - 1], DP0[i - 1] - A[i])
    print(DP0[-1])
