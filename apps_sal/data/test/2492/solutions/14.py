
import numpy as np
def resolve():
    n, k = list(map(int, input().split()))
    a = np.array(input().split(), dtype=np.int64)
    a.sort()

    zero = np.count_nonzero(a == 0)
    positive = a[a > 0]
    negative = a[a < 0]

    def count(x):  # 積が x 以下のペアは何個あるか？
        ans = 0
        if x >= 0:  # 片側が 0 の場合
            ans += n * zero
        ans += np.searchsorted(a, x // positive, side="right").sum()  # 片側が正の場合
        ans += n * len(negative) - np.searchsorted(a, -(-x // negative), side="left").sum()  # 片側が負の場合 切り上げは -(-a//b)
        ans -= np.count_nonzero(a * a <= x)  # 同じもの2つは選べない
        return ans // 2

    ok = 10 ** 18
    ng = -ok - 1
    while ok - ng > 1:  # 二分探索
        cen = (ok + ng) // 2
        if count(cen) >= k:
            ok = cen
        else:
            ng = cen
    print(ok)

def __starting_point():
    resolve()

__starting_point()
