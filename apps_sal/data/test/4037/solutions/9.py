from collections import namedtuple

n, r = list(map(int, input().split()))
plus = []
minus = []
Project = namedtuple('Project', 'value a b')
for _ in range(n):
    a, b = list(map(int, input().split()))
    if b >= 0:
        plus.append((a, b))
    else:
        minus.append(Project(max(0, a + b), a, b))
plus.sort()
minus.sort(reverse=True)
ans = 0
for a, b in plus:
    if r >= a:
        r += b
        ans += 1
dp = [[-1 for _ in range(60001)] for _ in range(len(minus) + 1)]
dp[0][r] = 0
for i in range(len(dp) - 1):
    for j in range(len(dp[0])):
        if dp[i][j] == -1:
            continue
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j + minus[i].b >= 0 and minus[i].a <= j:
            dp[i + 1][j + minus[i].b] = max(dp[i + 1][j + minus[i].b], dp[i][j] + 1)
ans += max(dp[-1])
print(ans)
