# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,Ma,Mb = map(int,input().split())
ABC = [tuple(map(int,input().split())) for _ in range(N)]

# dp[a][b] : Aタイプが ag, Bタイプが bg となる 最小コスト
inf = float("inf")
dp = [[inf for _ in range(401)] for _ in range(401)]
dp[0][0] = 0

for a,b,c in ABC:
    for i in range(400,-1,-1):
        for j in range(400,-1,-1):
            if dp[i][j] != inf:
                # 薬品を使った方が安ければ更新する
                dp[i+a][j+b] = min(dp[i+a][j+b], dp[i][j] + c)

ans = inf
for i in range(1,401):
    for j in range(1,401):
        # i : j == Ma : Mb なら コストを更新
        if i*Mb == j*Ma:
            ans = min(ans, dp[i][j])

print(ans if ans != inf else -1)
