def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 全探索するとN!なのでN=2000のときO(N^2000)となるので無理
    # DPで解く
    # dp[i][l] = 係数が大きい順にi個左右の端どちらにつめるか決めて、左をl回(右はn-l回)選んだときの指標最大値

    # 降順にAをソート+元のインデックスも保存しておく
    Awithidx = [[a,i] for i,a in enumerate(A)]
    sortedA = sorted(Awithidx, reverse=True)
    # DP
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        a = sortedA[i][0]
        idx = sortedA[i][1]
        for l in range(i+1):
            r = i-l
            dp[i+1][l] = max(dp[i+1][l], dp[i][l]+a*abs((N-r-1)-idx))
            dp[i+1][l+1] = max(dp[i+1][l+1], dp[i][l]+a*abs(l-idx))
    print((max(dp[N])))

main()

