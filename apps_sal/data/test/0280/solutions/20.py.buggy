from itertools import permutations
from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
w = list(map(int, input().split()))
lu = [list(map(int, input().split()))for _ in range(m)]
lu.sort(key=lambda x: x[1])
lu = [[0, lu[0][1]]] + lu
l = []
u = []
for ll, uu in lu:
    u.append(uu)
    if len(l):
        l.append(max(ll, l[-1]))
    else:
        l.append(ll)
if max(w) > min(u):
    print(-1)
    return

ans = 10**20
for p in permutations(w):
    x = [0] + list(p)
    for i in range(n):
        x[i + 1] += x[i]
    dp = [0] * n
    for i in range(n - 1):
        for j in range(i + 1, n):
            s = x[j + 1] - x[i]
            ll = l[max(bisect_left(u, s) - 1, 0)]
            dp[j] = max(dp[j], dp[i] + ll)
    ans = min(ans, dp[n - 1])
    # print(p,dp)
print(ans)
