(X, Y) = map(int, input().split())
mod = 10 ** 9 + 7
N = (X + Y) // 3
M = (N + X - Y) // 2
if (X + Y) % 3 != 0 or M < 0 or N < M:
    print(0)
else:
    ans = 1
    for m in range(1, M + 1):
        ans *= (N - M + m) * pow(m, mod - 2, mod)
        ans %= mod
    print(ans)
