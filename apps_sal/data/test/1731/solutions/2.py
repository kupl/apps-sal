(n, m) = list(map(int, input().split()))
mod = 10 ** 9 + 7
DP = [0] * (n + 1)
DP[0] = 1
for i in range(m):
    nxt = [0] * (n + 1)
    cnt = DP[0]
    for i in range(1, n + 1):
        cnt += DP[i]
        cnt %= mod
        nxt[i] = cnt
    DP = nxt
cnt = 0
ans = 0
for i in reversed(list(range(1, n + 1))):
    cnt += DP[n - i + 1]
    ans += DP[i] * cnt
    ans %= mod
print(ans)
