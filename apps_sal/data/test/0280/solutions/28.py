import itertools
import bisect

def f(i):
    if i == n:
        k = 0
        sumw = 0
        for j in range(n):
            if s[j]:
                k += pow2[j]
                sumw += w[j]
        sumwlist[k] = sumw
        return
    s[i] = 1
    f(i + 1)
    s[i] = 0
    f(i + 1)
    return

n, m = map(int, input().split())
w = list(map(int, input().split()))
vl = []
vlist = []
for _ in range(m):
    l, v = map(int, input().split())
    vl.append([v, l])
vl.sort()
for v, l in vl:
    vlist.append(v)
if vlist[0] < max(w):
    print(-1)
    return
maxl = [0] * (m + 1)
for i in range(m):
    maxl[i + 1] = max(maxl[i], vl[i][1])
s = [0] * n
pow2 = [1] * n
for i in range(n - 1):
    pow2[i + 1] = 2 * pow2[i]
sumwlist = [0] * (2 * pow2[-1] + 5)
f(0)
okl = [0] * (2 * pow2[-1] + 5)
for i in range(2 * pow2[-1]):
    okl[i] = maxl[bisect.bisect_left(vlist, sumwlist[i])]
ans = 1145141919810
for p in itertools.permutations(pow2):
    p = list(p)
    q = [0] * (n + 1)
    for i in range(n):
        q[i + 1] = p[i] + q[i]
    dp = [[0] * (n - 1) for _ in range(n - 1)]
    for i in range(n - 1):
        dp[0][i] = okl[q[i + 2] - q[i]]
    for i in range(1, n - 1):
        for j in range(n - 1 - i):
            dp[i][j] = okl[q[i + j + 2] - q[j]]
            for k in range(1, i + 1):
                dp[i][j] = max(dp[i][j], dp[k - 1][j] + dp[i - k][j + k])
    ans = min(ans, dp[n - 2][0])
print(ans)
