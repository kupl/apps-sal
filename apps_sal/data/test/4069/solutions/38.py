#今Xにいる、K回 D移動する
[X, K, D] = [int(i) for i in input().split()]
#正負で答え変化しないので、正に変える
X = abs(X)
if X - K*D > 0:
#原点に到達しないとき
    print(X-K*D)
#原点に到達するとき
else:
    #往復始める正の位置を求める
    time = int(X/D)
    start = X - D * time
    #残り移動回数を計算
    time_re = K - time
    #残り回数の偶奇で場合分け
    if time_re % 2 == 0:
        print(start)
    else:
        print(abs(start-D))
