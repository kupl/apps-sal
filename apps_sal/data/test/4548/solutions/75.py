n,m,x = map(int,input().split())
a = list(map(int,input().split()))

# 小さいほうの料金所の数
small_cost = 0
# 大きい方の料金所の数
big_cost = 0

# リストaの値とｘを比較して
for i in a:
    # ｘより小さいものをカウント
    if x > i:
        small_cost += 1
    # ｘより大きいものをカウント
    elif x < i:
        big_cost += 1
# 少ない方のカウントを出力
if small_cost <= big_cost:
    print(small_cost)
else:
    print(big_cost)
