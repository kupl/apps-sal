import numpy as np

N, K = list(map(int, input().split()))
A = np.sort(np.array(input().split(),np.int64))
z = A[A == 0]
p = A[A > 0]
n = A[A < 0]



def check(x):
    # x以下の数がK個以上ある時、Trueを返す
    count = 0 #最後に２で割る
    if x >= 0:
        count += len(z) * N
    count += (np.searchsorted(A, x//p, side='right')).sum()
    count += (N - np.searchsorted(A, (-x-1)//(-n), side='right')).sum()
    count -= np.count_nonzero(A * A <= x) #ペアなので自分自身は駄目
    assert count % 2 == 0
    count //= 2
    return count >= K

left = - 10 ** 19 # NG
right = 10 ** 19 # OK
while right > left + 1:
    mid = (left+right) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)

