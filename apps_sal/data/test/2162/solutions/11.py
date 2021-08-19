def LIS(X):
    N = len(X)
    P = [0] * N
    M = [0] * (N + 1)
    L = 0
    for i in range(N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if (X[M[mid]] < X[i]):
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        if (newL > L):
            L = newL

    S = []
    k = M[L]
    for i in range(L - 1, -1, -1):
        S.append(X[k])
        k = P[k]

    return len(S)  # [::-1]


k1, k2, k3 = list(map(int, input().split()))
a = []
for _ in range(3):
    a.extend(sorted(list(map(int, input().split()))))

print(k1 + k2 + k3 - LIS(a))

# 1 5 1
# 6
# 5 1 2 4 7
# 3

# 2 1 3
# 5 6
# 4
# 1 2 3
