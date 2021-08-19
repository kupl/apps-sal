a, b, c, d = map(int, input().split())
# 2つの面積をリスト化
area = [a * b, c * d]
# 面積のうち最大値を出力
print(max(area))
