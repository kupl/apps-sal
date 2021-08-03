'''
着想：大きいaほど左右の端に移動したい、小さいaを先に端にやるより必ず大きくなるから
問題：単純に貪欲に大きいaから左端(x-1)と右端(N-x)の大きい方に移動すると、
      残りのaの組み合わせ的に最適でない場合がある
      アイテムの左右端の単純な割り振りはO(2^N)
解決策の着想：大きい順のk個を(k=L+R)となる
    　　左L個右R個にどのように割り振っても(k+1)個目の最適な割り振り方は変わらない
解決策：アイテムk個左右に割り振る状態をdp[L][R]で保存O(N^2)
'''


def solve():
    N = int(input())
    A = [[a, i] for a, i in zip(map(int, input().split()), range(N))]
    A.sort(key=lambda a: a[0], reverse=True)

    dp = [[0] * (N + 1) for _ in range(N + 1)]  # 左からxマス右からyマス埋める
    for i in range(0, N):
        a, l = A[i]
        for x in range(0, i + 1):
            y = i - x  # 合計x+y=iマス既に埋まっている、次にi+1マス目を考える
            dp[x + 1][y] = max(dp[x + 1][y], dp[x][y] + a * abs(l - x))
            dp[x][y + 1] = max(dp[x][y + 1], dp[x][y] + a * abs(l - (N - y - 1)))

    print(max(dp[N - i][i] for i in range(N + 1)))


solve()
