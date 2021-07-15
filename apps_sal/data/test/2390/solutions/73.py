N, C = list(map(int, input().split()))
XV = [tuple(map(int, input().split())) for _ in range(N)]
XV.sort()

L = [0] * (N + 1)
S = 0
for i, (x, v) in enumerate(XV, start=1):
    S += v
    L[i] = max(L[i - 1], S - x)

R = [0] * (N + 1)
S = 0
for i, (x, v) in enumerate(XV[::-1], start=1):
    S += v
    R[i] = max(R[i - 1], S - (C - x))

ans = max(max(L), max(R))

S = 0
for i, (x, v) in enumerate(XV, start=1):
    S += v
    ans = max(ans, S - 2 * x + R[N - i])

S = 0
for i, (x, v) in enumerate(XV[::-1], start=1):
    S += v
    ans = max(ans, S - (C - x) * 2 + L[N - i])

print(ans)

