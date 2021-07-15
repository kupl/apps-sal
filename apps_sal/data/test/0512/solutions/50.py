def check(l, r):
    if (r - l) % 2 == 1:
        return False
    n = (r - l) // 2
    res = True
    for j in range(l, l + n):
        k = j + n
        res = res and P[j][k]
    return res

N = int(input())
F = [(0, '未')]*(2*N + 1)
for i in range(N):
    a, b = [int(x) for x in input().split()]
    if 1 <= a:
        if F[a][1] != '未':
            (print('No'));return
        F[a] = (i, '乗')
    if 1 <= b:
        if F[b][1] != '未':
            print('No');return
        F[b] = (i, '降')

P = [[False]*(2*N + 1) for _ in range(2*N + 1)]
for a in range(1, 2*N + 1):
    for b in range(a + 1, 2*N + 1):
        pair = (F[a][1], F[b][1])
        if pair in (('未', '未'), ('未', '降'), ('乗', '未')):
            P[a][b] = True
        if pair == ('乗', '降'):
            P[a][b] = F[a][0] == F[b][0]

dp = [False]*(N + 1)
dp[0] = True
for i in range(N + 1):
    if dp[i]:
        for j in range(i + 1, N + 1):
            if check(2 * i + 1, 2 * j + 1):
                dp[j] = True

print('Yes' if dp[N] else 'No')
