import heapq
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
B = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1 for _ in range(N + 10)]
dp[0] = 0
A.sort()
visited = [False for _ in range(N + 10)]
h = []
heapq.heappush(h, (0, 0))
while h:
    (now_n, keta) = heapq.heappop(h)
    if visited[now_n]:
        continue
    visited[now_n] = True
    for a in A:
        nxt_n = now_n + B[a]
        if nxt_n >= N + 10:
            continue
        dp[nxt_n] = max(dp[nxt_n], dp[now_n] + 1)
        heapq.heappush(h, (nxt_n, dp[now_n] + 1))
A.sort(reverse=True)
ANS = []
zan = N
for i in range(dp[N], 0, -1):
    bugf = True
    for a in A:
        if dp[zan - B[a]] == dp[zan] - 1:
            ANS.append(str(a))
            zan = zan - B[a]
            bugf = False
            break
    if bugf:
        print('bug...')
print(''.join(ANS))
