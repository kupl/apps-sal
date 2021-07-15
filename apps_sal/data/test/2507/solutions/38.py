
import numpy as np
def resolve():
    # 達成スコアを決める
    # 修行回数がK以下を達成できるスコアを二分探索
    def check(X):
        # 修行をしてスコアを最小化する
        a = X // F
        diff = np.maximum(A - a, 0)
        cnt = np.sum(diff)
        return cnt <= K

    N, K = list(map(int, input().split()))
    A = np.array(input().split(), np.int64)
    F = np.array(input().split(), np.int64)

    A.sort()
    F.sort()
    F = F[::-1]

    ok = 10 ** 12  # 最大スコア a: 10**6 * x:10**6
    ng = -1
    while ok - ng > 1:
        X = (ok + ng) // 2
        if check(X):
            ok = X
        else:
            ng = X

    print(ok)


def __starting_point():
    resolve()

__starting_point()
