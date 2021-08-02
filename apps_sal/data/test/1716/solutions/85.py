# 区間の問題は累積和か尺取り法
# 区間で条件を満たすものの個数→累積和
# 区間の数、条件を満たす区間の最大値最小値→尺取り法
# 今回は区間で条件を満たすものの総和→累積和
# 二つの端点を同時に扱わなくてはならない
# 列車の始まりが区間に含まれるかつ列車の終わりが区間に含まれて＋１である
# つまり二次元累積和を書けばいい
n, m, q = list(map(int, input().split()))
ruiseki = [[0 for i in range(n + 1)] for i in range(n + 1)]
for i in range(m):
    l, r = list(map(int, input().split()))
    ruiseki[l][r] = ruiseki[l][r] + 1
# 二次元累積和を計算する
for i in range(0, n + 1):
    for j in range(1, n + 1):
        ruiseki[i][j] = ruiseki[i][j] + ruiseki[i][j - 1]
for i in range(1, n + 1):
    for j in range(n + 1):
        ruiseki[i][j] = ruiseki[i - 1][j] + ruiseki[i][j]

# 各クエリに対して累積和を計算
for i in range(q):
    p, q = list(map(int, input().split()))
    print((ruiseki[q][q] - ruiseki[p - 1][q] - ruiseki[q][p - 1] + ruiseki[p - 1][p - 1]))
