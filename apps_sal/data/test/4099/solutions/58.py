# 高橋君は N科目のテストを受けます。各テストは K点満点であり、点数はそれぞれ 0以上の整数です。
# 高橋君は N−1科目のテストを既に受けており、i番目の科目のテストの点数は Ai点でした。
# 高橋君の目標は、N科目のテストの平均点を M点以上にすることです。
# 高橋君が目標を達成するためには、最後のテストで最低何点取る必要があるか出力してください。
# 達成不可能である場合は、代わりに -1 を出力してください。

# n(科目数)、m(平均点)、k(満点):標準入力
n, k, m = map(int, input().split())
a = list(map(int, input().split()))

# 最後のテストの最低点
last_score = sum(a)

# 最後の平均点の値
score = (n * m) - last_score

if score <= k:
    if score > 0:
        print(score)
    else:
        print(0)
else:
    print(-1)
