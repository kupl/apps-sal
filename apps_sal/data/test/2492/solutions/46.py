# https://maspypy.com/atcoder-%E5%8F%82%E5%8A%A0%E6%84%9F%E6%83%B3-2019-02-16abc-155
import numpy as np

N, K = list(map(int, input().split()))
A = np.array(list(map(int, input().split())))
A.sort()
G = A[A > 0]
Z = A[A == 0]
L = A[A < 0]

ok = 10 ** 18 + 1
ng = -10 ** 18 - 1

# x以下がK個以上であるxの最小値

while ok - ng > 1:
    mid = (ng + ok) // 2
    # mid以下のペアの個数を数える

    # 正のもののうち、mid以下のペアの個数を数える
    cg = np.searchsorted(A, mid // G, side="right").sum()

    # 負のもののうちmid以下のペアの個数を数える
    cl = (N - np.searchsorted(A, (mid + 1) // L, side="right")).sum()

    # 同じ数字同士の積がmid以下のものを数える
    d = np.count_nonzero(A * A <= mid)

    # 0がmid以下なら、それもプラスするために必要
    z = 0
    if mid >= 0:
        z += len(Z) * N

    c = cg + cl + z - d

    # 二重になっているので、割る
    c //= 2

    # mid以下のペアの個数がK個以上のとき
    if c >= K:
        ok = mid
    else:
        ng = mid

print(ok)
