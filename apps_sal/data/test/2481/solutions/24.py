import sys
input = sys.stdin.readline
def __starting_point():
    H,W = map(int,input().split())
    V = 10
    edges = []
    for i in range(10):
        c = list(map(int,input().split()))
        edges.append([(j,c[j]) for j in range(10)])
    INF = float("inf")
    dp = [[INF]*V for _ in range(V)]
    for i in range(V):
        for j, w in edges[i]:
            dp[i][j] = w

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    ans = 0
    for _ in range(H):
        for x in map(int,input().split()):
            if x >= 0:
                ans += dp[x][1]
    print(ans)
__starting_point()
