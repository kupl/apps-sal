import sys
import numpy as np

# 価値 x 以上の握手を全て行うとする
# 握手回数が決まる。左手ごとに集計できる。

N, M = list(map(int, sys.stdin.readline().rstrip().split()))
A = np.array(sys.stdin.readline().rstrip().split(), np.int64)

A.sort()  # A を昇順に並び替える

# x より価値が高くなる握手の総数
#  -> a に対して、相手は x - a が必要
#   -> A = [a0, a1, a2, ...] に対して、[x-a0の開始位置, x-a1の開始位置, x-a2の開始位置,...] を探す


def shake_cnt(x):
    # x 以上の握手を全て行うとして、握手の回数を数える行わない握手を数える
    X = np.searchsorted(A, x - A)  # ソートされたリストA に対して、x - A が挿入される位置を返す
    return N * N - X.sum()  # index の和は「小さい方」を指しているので、引く


# 二分探索  握手の回数が
left = 0  # 握手の回数がM以上
right = 10 ** 6  # 握手の回数がM未満 <- まだ足りない側
while 1 < right - left:  # left と right が隣り合ったら終了
    x = (left + right) // 2
    if shake_cnt(x) >= M:
        left = x
    else:
        right = x

# M回には届かないけれど、M回に限りなく近くなる価値 x = right
X = np.searchsorted(A, right - A)  # 各a in A が握手を行わない人数のArray
shake = N * N - X.sum()  # ここまでの握手回数

Acum = np.zeros(N + 1, np.int64)  # 人数 -> 累積和
# Acum = [a0, a0+a1, a0+a1+a2, ....] を計算して、ai さんが k番目以降と握手をすれば
Acum[1:] = np.cumsum(A)  # cumsum [1,2,3,4,5,6,...] -> [1,3,6,10,15,21,...]

# 右手の幸福度は ai * ((a0+a1+...a(n-1)) - (a(k-1)+...+a(n-1))) を得られる
# 左手の幸福度は 回数だけで決まる（何人と握手とするか）
happy = (Acum[-1] - Acum[X]).sum() + (A * (N - X)).sum()

happy += (M - shake) * left  # 不足分。1回の価値は M とわかっている

print(happy)
