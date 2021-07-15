def popcount(i):
    assert 0 <= i < 0x100000000
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

N, T = map(int, input().split())
TG = [list(map(int, input().split())) for _ in range(N)]
mod = 10**9+7


dp = [[0]*(2**N) for _ in range(4)]
for i in range(1, 4):
    dp[i][0] = 1

for S in range(2**N):
    if popcount(S) == 1:
        dp[TG[(S&(-S)).bit_length() - 1][1]][S] = 1
    for i in range(1, 4):
        for j in range(N):
            if S & (2**j) or i == TG[j][1]:
                continue
            dp[TG[j][1]][S|(2**j)] = (dp[TG[j][1]][S|(2**j)] + dp[i][S]) % mod

table = [0]*(2**N)
for S in range(2**N):
    table[S] = sum(TG[j][0] for j in range(N) if 2**j & S)
    
ans = 0
for S in range(2**N):
    if table[S] == T:
        for i in range(1, 4):
            ans = (ans + dp[i][S]) % mod

print(ans)
