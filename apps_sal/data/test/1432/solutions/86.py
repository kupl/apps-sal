N = int(input())
A = list(map(int, input().split()))
x = [None] * N
sm = 0
sign = 1
for i in range(N):
    sm += sign * A[i]
    sign *= -1
x[0] = sm // 2
for i in range(1, N):
    x[i] = A[i - 1] - x[i - 1]
print(*map(lambda a: a * 2, x))
