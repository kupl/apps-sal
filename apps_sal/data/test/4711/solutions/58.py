# 066A
# 1.値を正しく取得
a, b, c = (int(x) for x in input().split())

# 2.正しく処理
gokei1 = a + b
gokei2 = a + c
gokei3 = b + c

resalt = [gokei1, gokei2, gokei3]

print(min(resalt))
