A, B, X = map(int, input().split())
K = 0
# 桁数K検索
while A * 10**K + B * K < X:
    K += 1
# BNを引き、ANを求めてAで切捨除算
# 取引できる最大値を超えないようにmin
print(min((X - B * K) // A, 10**9))
