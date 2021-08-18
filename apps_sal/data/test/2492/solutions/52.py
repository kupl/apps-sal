import sys
import numpy as np

N, K = map(int, sys.stdin.readline().rstrip().split())
A = np.array(sys.stdin.readline().rstrip().split(), np.int64)

A = np.sort(A)
zero = A[A == 0]
pos = A[A > 0]
neg = A[A < 0]


def f2(x):
    """
    積が x 以下になるペアの個数を返す

    - (i,j) と (j,i), (i,i) の重複を許して後で調整
    - A = [a_0, a_1, a_2, ... ,a_n-1] で、
         負 ～ 0 ～ 正 まで混ざった状態で
         target k と掛け合わせて x 以下になる場所 (index) を探す
    -           \__-5_-1__0_0_...__1___2
      a_0   = -5|  25  5  0 0 ... -5 -10
      a_1   = -1|   5  1  0 0 ... -1  -2
      a_2   =  0|   0  0  0 0 ...  0   0
      a_3   =  0|   0  0  0 0 ...  0   0
      a_4   =  1|  -5 -1  0 0 ...  1   2
      .....     |
      a_n-1 =  2| -10 -2  0 0 ...  2   4
    """

    cnt_tpl = 0

    B = A.copy()
    B = -B
    B.sort()
    cnt_tpl += np.searchsorted(B, x // (-neg), side='right').sum()

    if x >= 0:
        cnt_tpl += len(zero) * N

    cnt_tpl += np.searchsorted(A, x // pos, side='right').sum()

    cnt_tpl -= np.count_nonzero(A * A <= x)

    assert cnt_tpl % 2 == 0
    return cnt_tpl // 2


left = -10 ** 18
right = 10 ** 18
while left + 1 < right:
    x = (left + right) // 2
    if f2(x) >= K:
        right = x
    else:
        left = x


print(right)
