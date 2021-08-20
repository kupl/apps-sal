(N, K) = map(int, input().split())
mod = 10 ** 9 + 7
Ans = 0
for m in range(K, N + 2):
    maxi = m * (N - m + 1 + N) / 2
    mini = m * (0 + m - 1) / 2
    Ans += int(maxi - mini + 1)
    Ans %= mod
print(Ans)
