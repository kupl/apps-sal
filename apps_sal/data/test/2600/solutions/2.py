def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dc = [[0, 0] for _ in range(0 + 0, n - 1 + m - 1 + 1)]
    for i in range(n):
        for j in range(m):
            dc[i + j][a[i][j]] += 1
    ans = 0
    for i in range(len(dc) // 2):
        j = len(dc) - 1 - i
        ans += min(dc[i][0] + dc[j][0], dc[i][1] + dc[j][1])
    print(ans)

t = int(input())
for _ in range(t):
    solve()
