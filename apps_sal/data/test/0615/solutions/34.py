import bisect

N = int(input())
A = list(int(a) for a in input().split())

Acum = [0] * (N + 1)
for i in range(N):
    Acum[i + 1] = Acum[i] + A[i]

ans = 10**18
for i in range(2, N - 1):
    B = bisect.bisect_left(Acum, Acum[i] // 2) - 1
    if abs(Acum[B] * 2 - Acum[i]) > abs(Acum[B + 1] * 2 - Acum[i]):
        B += 1
    if B == i:
        B -= 1
    elif B == 0:
        B += 1
    P = Acum[B]
    Q = Acum[i] - Acum[B]
    D = bisect.bisect_left(Acum, Acum[i] + (Acum[-1] - Acum[i]) // 2) - 1
    if abs(Acum[D] * 2 - Acum[i] - Acum[-1]) > abs(Acum[D + 1] * 2 - Acum[i] - Acum[-1]):
        D += 1
    if D == N:
        D -= 1
    elif D == i:
        D += 1
    R = Acum[D] - Acum[i]
    S = Acum[-1] - Acum[D]
    mi = min(P, Q, R, S)
    ma = max(P, Q, R, S)
    ans = min(ans, abs(ma - mi))
print(ans)
