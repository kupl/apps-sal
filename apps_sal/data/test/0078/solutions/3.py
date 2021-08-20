def popcount(i):
    assert 0 <= i < 4294967296
    i = i - (i >> 1 & 1431655765)
    i = (i & 858993459) + (i >> 2 & 858993459)
    return ((i + (i >> 4) & 252645135) * 16843009 & 4294967295) >> 24


(N, T) = map(int, input().split())
TG = [list(map(int, input().split())) for _ in range(N)]
mod = 10 ** 9 + 7
dp = [[0] * 2 ** N for _ in range(4)]
for i in range(1, 4):
    dp[i][0] = 1
for S in range(2 ** N):
    if popcount(S) == 1:
        dp[TG[(S & -S).bit_length() - 1][1]][S] = 1
    for i in range(1, 4):
        for j in range(N):
            if S & 2 ** j or i == TG[j][1]:
                continue
            dp[TG[j][1]][S | 2 ** j] = (dp[TG[j][1]][S | 2 ** j] + dp[i][S]) % mod
table = [0] * 2 ** N
for S in range(2 ** N):
    table[S] = sum((TG[j][0] for j in range(N) if 2 ** j & S))
ans = 0
for S in range(2 ** N):
    if table[S] == T:
        for i in range(1, 4):
            ans = (ans + dp[i][S]) % mod
print(ans)
