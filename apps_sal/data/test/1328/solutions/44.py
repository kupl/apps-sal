import copy
n, ma, mb = map(int, input().split())
a, b, c = [0] * n, [0] * n, [0] * n
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())

dp = [[float('inf')] * (sum(b) + 1) for _ in range(sum(a) + 1)]
dp[0][0] = 0
step = set([(0, 0)])

for i in range(n):
    ai, bi = a[i], b[i]

    s = step.copy()
    tempdp = copy.deepcopy(dp)
    for si in s:
        if dp[si[0] + ai][si[1] + bi] > dp[si[0]][si[1]] + c[i]:
            tempdp[si[0] + ai][si[1] + bi] = dp[si[0]][si[1]] + c[i]
            step.add((si[0] + ai, si[1] + bi))

    dp = tempdp[:]

ans = float('inf')
for i in range(1, min(sum(a) // ma, sum(b) // mb) + 1):
    ans = min(ans, dp[ma * i][mb * i])

if ans == float('inf'):
    print(-1)
else:
    print(ans)
