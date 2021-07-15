X,K,D = list(map(int, input().split()))

# X > 0 として良い
X = abs(X)

# 原点に向かう
c = min(K, X//D)
K -= c
X -= D * c

# 移動できなければ終了
if K == 0:
    print(X)
else:
    # 行ったり来たりする
    if K%2:
        print((abs(X-D)))
    else:
        print(X)

