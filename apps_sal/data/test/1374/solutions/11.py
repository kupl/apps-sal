import numpy as np
from collections import defaultdict

N = int(input())
A = np.array(input().split(), dtype=np.int32)
total_medians = N * (N + 1) // 2
# n件のデータ
# (上側中央値 >= x) iff (a > x となる a が(n-1)//2以下)


def test(x):
    # 「答はx以下である」
    # 「xより真に大きな区間中央値が(total_medians-1)//2個以下」
    # xより真に大きな値を1、他を-1とする。
    # 1の個数が-1の個数以上になっている区間
    current = 0  # 累積和
    memo = defaultdict(int)  # 過去の累積和の分布, incl empty
    memo[0] = 1
    cnt_below = 1  # sum memo[y] for y <= x
    result = 0
    for a in A:
        if a > x:
            current += 1
            cnt_below += memo[current]
        else:
            cnt_below -= memo[current]
            current -= 1
        result += cnt_below
        memo[current] += 1
        cnt_below += 1
    return result <= (total_medians - 1) // 2


AA = sorted(A)
left = -1  # 答はAA[left]より大きい
right = len(AA) - 1  # 答はAA[right]以下である
while right - left > 1:
    mid = (left + right) // 2
    if test(AA[mid]):
        right = mid
    else:
        left = mid

answer = AA[right]
print(answer)
