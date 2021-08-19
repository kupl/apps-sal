import heapq
(n, m) = map(int, input().split())
ans = [0] * n
ary = []
dp = [[0] * n for i in range(n)]
tmp = 0
while tmp < m:
    (s, d, c) = map(int, input().split())
    s -= 1
    d -= 1
    ans[d] = m + 1
    ary.append((s, d, c + 1, tmp))
    dp[s][d] = c
    tmp += 1
d = 2
while d < n:
    l = 0
    while l + d < n:
        r = l + d
        dp[l][r] += dp[l + 1][r] + dp[l][r - 1] - dp[l + 1][r - 1]
        if dp[l][r] > d:
            print(-1)
            quit(0)
        l += 1
    d += 1
l = 0
pos = 0
sary = sorted(ary)
que = []
while l < n:
    while pos < m and sary[pos][0] == l:
        heapq.heappush(que, [sary[pos][1], sary[pos][2], sary[pos][3]])
        pos += 1
    if ans[l] > 0:
        l += 1
        continue
    if que.__len__() == 0:
        l += 1
        continue
    head = heapq.heappop(que)
    if head[1] + l - 1 > head[0]:
        print(-1)
        quit(0)
    head[1] -= 1
    ans[l] = head[2] + 1
    if head[1] > 1:
        heapq.heappush(que, head)
    l += 1
if que.__len__() > 0 or pos < m:
    print(-1)
else:
    print(*ans)
