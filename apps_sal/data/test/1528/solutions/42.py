(N, X) = list(map(int, input().split()))


def solve(N, X):
    if X == 0:
        return 0
    if N == 0:
        return X
    if X < 2 ** (N + 1) - 1:
        return solve(N - 1, X - 1)
    elif X == 2 ** (N + 1) - 1:
        return 2 ** N
    elif X < 2 ** (N + 2) - 3:
        return 2 ** N + solve(N - 1, X - 2 ** (N + 1) + 1)
    else:
        return 2 ** (N + 1) - 1


print(solve(N, X))
