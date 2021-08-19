(N, X) = list(map(int, input().split()))
L = [1 for _ in range(N + 1)]
S = [1 for _ in range(N + 1)]
for n in range(1, N + 1):
    L[n] = L[n - 1] * 2 + 3
    S[n] = S[n - 1] * 2 + 1


def rec(level, K):
    if level == 0:
        return 1
    if K == 1:
        return 0
    elif K <= L[level - 1] + 1:
        return rec(level - 1, K - 1)
    elif K == L[level - 1] + 2:
        return S[level - 1] + 1
    elif K <= L[level - 1] * 2 + 2:
        return rec(level - 1, K - L[level - 1] - 2) + S[level - 1] + 1
    else:
        return S[level - 1] * 2 + 1


print(rec(N, X))
