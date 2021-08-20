from sys import stdin
input = stdin.readline


def add_mod(a, b):
    return (a % c + b % c) % c


N = 101
(n, q, c) = list(map(int, input().split()))
c += 1
star = [list(map(int, input().split())) for _ in range(n)]
view = [list(map(int, input().split())) for _ in range(q)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(11)]
for mod in range(11):
    for (i, j, k) in star:
        dp[mod][i][j] += add_mod(k, mod)
for mod in range(11):
    for i in range(1, N):
        for j in range(1, N):
            dp[mod][i][j] += dp[mod][i][j - 1]
all_res = []
for (t, x1, y1, x2, y2) in view:
    tem = 0
    for i in range(x1, x2 + 1):
        tem += dp[t % c][i][y2] - dp[t % c][i][y1 - 1]
    all_res.append(str(tem))
print('\n'.join(all_res))
