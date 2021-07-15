from sys import stdin
from functools import lru_cache
N = int(stdin.readline().rstrip())
K = int(stdin.readline().rstrip())

@lru_cache(None)
def f(N, K):
    #大きい桁から小さい桁へ
    if K < 0:
        return 0
    if N < 10:
        if K == 0:
            # 0のみ
            return 1
        elif K == 1:
            # 例えばN=4 なら0でないものが1,2,3,4の合計4個存在
            return N
        else:
            return 0
    q, r = divmod(N, 10)
    ret = 0
    if K >= 1:
        # 1の位が0以外の場合Kを消費する
        ret += f(q, K-1) * r
        ret += f(q-1, K-1) * (9-r)
    # 1の位が0の場合
    ret += f(q, K)
    return ret

print(f(N, K))
