def f(l, r):
    L = r - l
    if L % 2:
        return 0
    for i in range(l, l + L // 2):
        if R[P[i]] >= r and R[P[i]] + 1:
            return 0
        if (P[i] == Q[L // 2 + i] or P[i] * Q[L // 2 + i] == 0) * (Q[i] + P[L // 2 + i] == 0):
            continue
        return 0
    return 1


N = int(input())
M = 2 * N
P, Q, R, d = [0] * M, [0] * M, [-1] * (N + 1), [0] * (M + 1)
for i in range(1, N + 1):
    A, B = map(int, input().split())
    if (A + 1 and P[A - 1] != 0) or (B + 1 and Q[B - 1]):
        print("No")
        return
    if A + 1:
        P[A - 1] = i
    if B + 1:
        Q[B - 1] = i
        R[i] = B - 1
d[0] = 1
for i in range(2, M + 1):
    for j in range(i):
        if d[j] * f(j, i):
            d[i] = 1
            break
print('NYoe s'[d[-1]::2])
