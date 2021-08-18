
N = int(input())
A = list(int(a) for a in input().split())

a = A[0]
b = A[1]
S = a + b
X = 0
for i in range(2, N):
    X ^= A[i]

dp = [[[-1] * 2 for i in range(2)] for j in range(50)]
dp[0][0][0] = 0

for i in range(49):
    cur_s = S >> i & 1
    cur_x = X >> i & 1
    cur_a = a >> i & 1
    for j, k in ((0, 0), (0, 1), (1, 0), (1, 1)):
        if dp[i][j][k] == -1:
            continue
        for p, q in ((0, 0), (0, 1), (1, 0), (1, 1)):
            if p ^ q != cur_x:
                continue
            if (p + q + j) & 1 != cur_s:
                continue
            ni = i + 1
            nj = 0
            if (p + q + j) >= 2:
                nj = 1
            if cur_a < p:
                nk = 1
            elif cur_a > p:
                nk = 0
            else:
                nk = k
            dp[ni][nj][nk] = max(dp[ni][nj][nk], dp[i][j][k] | (1 << i) * p)

tmp = dp[49][0][0]
if tmp == 0 or tmp == -1:
    print(-1)
else:
    print(a - tmp)
