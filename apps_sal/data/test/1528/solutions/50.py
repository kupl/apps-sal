N, X = map(int, input().split())
A = [1] * (N + 1)
P = [1] * (N + 1)
for i in range(1, N + 1):
    P[i] = 2 * P[i - 1] + 1
    A[i] = 2 * P[i] - 1


def f(N, X):
    if X == 1:
        if N == 0:
            return 1
        else:
            return 0
    elif 1 < X <= 1 + A[N - 1]:
        return f(N - 1, X - 1)
    elif X == 2 + A[N - 1]:
        return P[N - 1] + 1
    elif 2 + A[N - 1] < X <= 2 + 2 * A[N - 1]:
        return P[N - 1] + 1 + f(N - 1, X - 2 - A[N - 1])
    else:
        return 2 * P[N - 1] + 1


print(f(N, X))
