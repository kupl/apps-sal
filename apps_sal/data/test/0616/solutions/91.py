n, m = list(map(int, input().split()))
dp = [2**63] * 4096
dp[0] = 0
for i in range(m):
    a, b = list(map(int, input().split()))
    mask = 0
    c = list(map(int, input().split()))
    for i in c:
        mask |= (1 << i - 1)
    nxtdp = dp[:]
    for j in range(1 << n):
        if dp[j] < 2 ** 63:
            nxtdp[j | mask] = min(nxtdp[j | mask], dp[j] + a)
    dp = nxtdp
print((dp[(1 << n) - 1] if dp[(1 << n) - 1] < 2**63 else -1))
