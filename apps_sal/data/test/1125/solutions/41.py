N = int(input())
A, B, *C = list(map(int, input().split()))
X = 0
for c in C:
    X ^= c
S = A + B

K = 43
dp = [[[-1] * 2 for _ in range(2)] for _ in range(K)]
dp[0][0][0] = 0

for i in range(K - 1):
    cx = (X >> i) & 1
    cs = (S >> i) & 1
    ca = (A >> i) & 1
    for j in range(2):
        for k in range(2):
            if dp[i][j][k] == -1:
                continue
            for na in range(2):
                for nb in range(2):
                    if (na ^ nb) != cx:
                        continue
                    ns = na + nb + j
                    if ns % 2 != cs:
                        continue
                    nj = ns // 2
                    if ca < na:
                        nk = 1
                    elif ca == na:
                        nk = k
                    else:
                        nk = 0
                    dp[i + 1][nj][nk] = max(dp[i + 1][nj][nk], dp[i][j][k] + 2**i * na)
a = dp[-1][0][0]
if a == 0 or a == -1:
    print(-1)
else:
    print(A - a)
