h, w, d = map(int, input().split())
a = {}
for y in range(h):
    line = list(map(int, input().split()))
    for x in range(len(line)):
        a[line[x] - 1] = (y, x)

# 問題の考え方
# DP的な感じで解ける
# まずGridになっているが、1次元の配列として考える 3*3(=9マスある状態) なら
#   1,2,3,4,5,6,7,8,9
# このときに数値の低い方から高い方へいくとゴールにつく(Ri-LiがDの倍数であること)が保証されるので最後の数字へ向かうときにかかるコストを考える(以下、3*3の例)
#   D=2としたときに、9はこれ以上進めないので、コスト0, 8もそれ以上進めないので コスト0, 7は9に行けるので9のコスト+7から9へ向かうコストで算出可能
#   また、5~9へのコストは1~9へのコスト引く1~5までのコストとなるので累積和的に答えを算出することが可能

num = len(a)
dp = [0] * num
for i in range(num - 1, -1, -1):
    if i + d <= num - 1:
        x, y = a[i]
        px, py = a[i + d]
        dp[i] = dp[i + d] + abs(x - px) + abs(y - py)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(dp[l] - dp[r])
