from collections import deque
(n, m) = map(int, input().split())
s = input()
dp = [-1 for _i in range(n + 1)]
dp[0] = 0
f = 0
q = deque([0])
c = 0
for i in range(1, n + 1):
    if s[i] == '0':
        c = 0
        while i - f > m:
            f = q.popleft()
        dp[i] = f
        q.append(i)
    elif c < m - 1:
        c += 1
    else:
        break
if dp[n] >= 0:
    r = []
    p = n
    while p > 0:
        nex = dp[p]
        r.append(p - nex)
        p = nex
    print(*r[::-1])
else:
    print(-1)
