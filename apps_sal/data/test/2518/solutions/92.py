
from math import ceil
def resolve():
    def chick(k):
        cnt = 0
        for i in range(N):
            h = ceil((H[i] - B * k) / (A - B))
            cnt += max(0, h)
        return cnt <= k

    N, A, B = list(map(int, input().split()))
    H = [int(input()) for _ in range(N)]

    # 最小の攻撃回数を求める
    # 魔法攻撃の回数をkとした時、すべての魔物は少なくともkBの体力が削られている
    # H[i] - kB > 0 であるような各iについて、その敵に対してA-Bの攻撃を何回当てれば体力が0になるかが算出される。
    # 上記の計算：(H[i] - kB) / (A-B) (ただし切り上げ)を計算して和を取る
    ok = 10 ** 10
    ng = 0
    while ok - ng > 1:
        k = (ok + ng) // 2
        if chick(k):
            ok = k
        else:
            ng = k

    print(ok)


def __starting_point():
    resolve()

__starting_point()
