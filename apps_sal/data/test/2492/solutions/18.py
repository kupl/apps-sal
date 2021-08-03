import numpy as np
N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))
A = np.sort(A)

G = A[A > 0]
Z = A[A == 0]
L = A[A < 0]

l, r = 10**18, -10**18

while l - r > 1:
    # 「積がm以下になるペアの数」を調べる。
    m = (l + r) // 2

    # A[A > 0]内から条件を満たすものの数?
    Pk = np.searchsorted(A, m // G, side="right").sum()

    # A[A < 0]内から条件を満たすものの数?
    Nk = (N - np.searchsorted(A, (-m - 1) // (-L), side="right")).sum()

    # 同じ要素同士の積は重複しているため、条件を満たしていたら減らす
    duplicate = np.count_nonzero(A * A <= m)

    # A[0]内から条件を満たすものの数?
    Zk = 0
    if m >= 0:
        Zk += len(Z) * N

    # 条件を満たす要素の数を合わせる
    k = Pk + Nk + Zk - duplicate

    # 全要素が二重になっている。重複要素を削除
    k //= 2

    # 条件を満たす要素数kがK個以上ならmを低く、Kより少ないならmを高くする
    if k >= K:
        l = m
    else:
        r = m
# lとrが一致すればmが一意に定まる
print(l)
