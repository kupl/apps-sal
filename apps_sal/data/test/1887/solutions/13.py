def gns():
    return list(map(int, input().split()))


n = int(input())
ps = []
ps.append(gns())
ps.append(gns())
dp = [[0] * 2 for i in range(n)]


def get(i, t):
    if i < 0:
        return 0
    else:
        return dp[i][t]


ans = 0
for i in range(n):
    for t in range(2):
        mx = max(get(i - 1, 1 - t), get(i - 2, 1 - t))
        dp[i][t] = mx + ps[t][i]
        ans = max(ans, dp[i][t])
print(ans)
