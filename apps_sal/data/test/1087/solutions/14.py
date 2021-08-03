N, K = map(int, input().split())
A = list(map(int, input().split()))

L = 40
bc = [0] * L
for i in range(L):
    for a in A:
        if a & (1 << i):
            bc[i] += 1

dp = [[-1, -1] for _ in range(L + 1)]
dp[L][0] = 0
for i in range(L - 1, -1, -1):
    c = (K >> i) & 1
    for l in range(2):
        if dp[i + 1][l] < 0:
            continue
        for d in range(2):
            if l == 0 and d > c:
                continue
            nl = 0 if l == 0 and d == c else 1
            dp[i][nl] = max(dp[i][nl], dp[i + 1][l] + 2**i * (N - bc[i] if d else bc[i]))

print(max(dp[0]))
