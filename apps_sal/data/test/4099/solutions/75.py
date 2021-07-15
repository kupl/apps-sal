'''
問題：
    高橋君は N 科目のテストを受けます。
    各テストは K 点満点であり、点数はそれぞれ 0 以上の整数です。

    高橋君は N−1 科目のテストを既に受けており、
    i 番目の科目のテストの点数は Ai 点でした。

    高橋君の目標は、N 科目のテストの平均点を M 点以上にすることです。
    高橋君が目標を達成するためには、最後のテストで最低何点取る必要があるか出力してください。
    達成不可能である場合は、代わりに -1 を出力してください。
'''

'''
制約：
    2 ≦ N ≦ 100
    1 ≦ K ≦ 100
    1 ≦ M ≦ K
    0 ≦ Ai ≦ K
    入力中のすべての値は整数である
'''
# class Test:
#     points = []
#     def __init__(self, point):
#         self.point = point
#
#     def add_test(self):
#         self.points.append(self)
#
#     def lasttest_min(self, target_point)   -> int:
#         target_point - ave(points)

# 標準入力から N, K, M, Ai の値を取得する
n, k, m = list(map(int, input().split()))
a = list(map(int, input().split()))

target_ponits = m * n # 目標に必要な合計点数
need_point_n = target_ponits - sum(a)   # N番目のテストで目標達成に必要な点数

result = "ret"
if need_point_n > k:
    result = -1
else:
    if need_point_n < 0:    # N番目が 0点でも目標達成できる場合
        result = 0
    else:
        result = need_point_n

print(result)

