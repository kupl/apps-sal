# N(科目数)、M(平均点)、K(満点):標準入力
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# 最後のテストの最低点
worst_score = sum(A)

# 最後の平均点の値
score = (N * M) - worst_score

if score <= K:
    if score > 0:
        print(score)
    else:
        print(0)
else:
    print(-1)
