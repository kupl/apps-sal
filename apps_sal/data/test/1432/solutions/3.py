N = int(input())
A = list(map(int, input().split()))
S = 0
sign = 1
for i in range(N):
    S += sign * A[i]
    sign *= -1
for i in range(N):
    print(S, end=' ' * (i < N - 1))
    S *= -1
    S += 2 * A[i]
print()
