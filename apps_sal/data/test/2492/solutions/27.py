import numpy as np
n, k = list(map(int, input().split()))

# np.int64をつけないと、後でA**2を計算したときに桁あふれする
A = np.array(sorted(list(map(int, input().split()))), np.int64)
posA = A[A > 0]  # 正の数のみの配列
negA = A[A < 0]  # 負の数のみの配列
z = (A == 0).sum()  # 0の個数

left = -10**18
right = 10**18

while left + 1 < right:
    num = (left + right) // 2
    # ペア積の配列の中で、numより小さいものの数を数えていく。
    count = 0  # まずは0で初期化する。
    # もしnumが0以上であれば、積がゼロになるペア積の数を足しこむ
    if num >= 0:
        # この段階では値がゼロのものについて自分との積をあえてカウントする
        count += z * n
    # 正の数に対して、かけてもnumを超えない最大の数字のリスト
    limit_pos = num // posA
    # limit_posの各数字を下回る数がAの中に何個あるかのリスト
    limit_idx = np.searchsorted(A, limit_pos, side='right')
    count += limit_idx.sum()

    # 負の数に対して、かけてもnumを超えない最大の数字のリスト
    limit_neg = -(-num // negA)
    # limit_negの各数字を下回る数がAの中に何個あるかのリスト
    limit_idx = n - np.searchsorted(A, limit_neg, side='left')
    count += limit_idx.sum()

    duplicate_cases = (A ** 2 <= num).sum()

    count -= duplicate_cases
    count //= 2

    if count >= k:
        right = num
    else:
        left = num

print(right)
