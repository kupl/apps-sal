N, M = map(int, input().split())
COST = []
B = []
C = []
C_bit = []
INF = 10**18
dp = [INF] * (1 << N)
dp[0] = 0

for _ in range(M):
    a, b = map(int, input().split())
    C.append(list(map(int, input().split())))
    COST.append(a)
    B.append(b)

for i in range(M):
    bit = ['0'] * N
    for j in range(B[i]):
        bit[C[i][j] - 1] = '1'
    bit_int = int(''.join(bit), 2)
    C_bit.append(bit_int)

for cost, c in zip(COST, C_bit):
    for i in range(1 << N):
        j = i | c
        d = dp[i] + cost
        if dp[j] > d:
            dp[j] = d

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
