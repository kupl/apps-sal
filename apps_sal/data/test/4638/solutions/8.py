import sys
input = sys.stdin.readline

n, c = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

TIME0 = [0] * n
TIME1 = [0] * n

TIME1[0] = c

for i in range(1, n):
    TIME0[i] = min(TIME0[i - 1], TIME1[i - 1]) + A[i - 1]
    TIME1[i] = min(TIME0[i - 1] + c + B[i - 1], TIME1[i - 1] + B[i - 1])

ANS = [min(TIME0[i], TIME1[i]) for i in range(n)]
print(*ANS)
