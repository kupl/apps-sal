import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

A_INV = [-1] * n
for i in range(n):
    A_INV[A[i] - 1] = i

L = list(range(-1, n - 1))
R = list(range(1, n + 1))

USELIST = [0] * n
ANS = [0] * n
NOW = 1

for a in A_INV[::-1]:
    if USELIST[a] == 1:
        continue
    USELIST[a] = 1
    ANS[a] = NOW

    if 0 <= a < n and 0 <= L[a] < n:
        R[L[a]] = R[a]

    if 0 <= a < n and 0 <= R[a] < n:
        L[R[a]] = L[a]

    r = a
    for step in range(k):
        r = R[r]
        if r < 0 or r >= n:
            break
        ANS[r] = NOW
        USELIST[r] = 1

        if 0 <= r < n and 0 <= L[r] < n:
            R[L[r]] = R[r]

        if 0 <= r < n and 0 <= R[r] < n:
            L[R[r]] = L[r]

    l = a
    for step in range(k):
        l = L[l]
        if l < 0 or l >= n:
            break
        ANS[l] = NOW
        USELIST[l] = 1

        if 0 <= l < n and 0 <= L[l] < n:
            R[L[l]] = R[l]

        if 0 <= l < n and 0 <= R[l] < n:
            L[R[l]] = L[l]

    NOW = 3 - NOW

print("".join(map(str, ANS)))
