import math


def takoyaki():
    # 入力
    N, X, T = map(int, input().split())
    # 処理
    count = math.ceil(N / X)
    return count * T


result = takoyaki()
print(result)
