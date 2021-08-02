from collections import deque
N = int(input())
mima = [-1] + list(map(int, input().split()))
par = [-1, -1] + list(map(int, input().split()))
leaf = set(range(1, N + 1))
cld = [0] * (N + 1)
for p in par:
    cld[p] += 1
    if p in leaf:
        leaf.remove(p)
dp = [0] * (N + 1)
for i in leaf:
    dp[i] = 1

Q = deque(list(leaf))
visited = leaf.copy()
while Q:
    vn = Q.pop()
    if vn == 1:
        break
    pv = par[vn]
    if mima[pv] == 1:
        if not dp[pv]:
            dp[pv] = dp[vn]
        else:
            dp[pv] = min(dp[pv], dp[vn])
        cld[pv] -= 1
        if not cld[pv]:
            Q.appendleft(pv)
    else:
        if not dp[pv]:
            dp[pv] = dp[vn]
        else:
            dp[pv] += dp[vn]
        cld[pv] -= 1
        if not cld[pv]:
            Q.appendleft(pv)
print(len(leaf) - dp[1] + 1)
