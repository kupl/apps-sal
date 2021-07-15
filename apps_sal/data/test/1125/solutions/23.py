N = int(input())
A = list(map(int, input().split()))

# a = A_1, b = A_2, x = A_3 ^ ... ^ A_N, s = a + b とする
a, b = A[0], A[1]
x = 0
for i in range(2, N):
    x ^= A[i]
s = a + b

M = 42
# dp[桁][繰り上げフラグ][これまでの桁でAより大きいフラグ] := Aとなり得る値の最大値
dp = [[[-1] * 2 for _ in range(2)] for _ in range(M + 1)]
dp[0][0][0] = 0
v = 1
for i in range(M):
    cs = s & 1
    cx = x & 1
    ca = a & 1
    for j in range(2):
        for k in range(2):
            if dp[i][j][k] == -1:
                continue
            for na in range(2):
                for nb in range(2):
                    # 条件1: na ^ nb = x
                    if na ^ nb != cx:
                        continue
                    # 条件2: na + nb = S
                    ns = na + nb + j
                    if ns & 1 != cs:
                        continue
                    
                    # 遷移先のi, j, kを求める
                    ni = i + 1
                    nj = 1 if ns >= 2 else 0
                    if na > ca:
                        nk = 1
                    elif na < ca:
                        nk = 0
                    else:
                        nk = k
                    
                    # 遷移先を最大化
                    dp[ni][nj][nk] = max(dp[ni][nj][nk], dp[i][j][k] + na * v)
    s >>= 1
    x >>= 1
    a >>= 1
    v <<= 1

amax = dp[M][0][0]
if amax <= 0:
    print((-1))
else:
    print((A[0] - amax))

