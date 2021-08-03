X, K, D = map(int, input().split())

if X - K * D >= 0:
    ans = abs(X - K * D)
elif X + K * D <= 0:
    ans = abs(X + K * D)
else:
    n = int(abs(X - K * D) / (2 * D))
    ans = min(abs(X - K * D + n * 2 * D), abs(X - K * D + (n + 1) * 2 * D))

print(ans)
