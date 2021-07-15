#080A
# 1.値を正しく取得
a, b, c = (int(x) for x in input().split())

# 2.正しく処理
plan1 = a * b
plan2 = c

resalt=[plan1,plan2]

print(min(resalt))
