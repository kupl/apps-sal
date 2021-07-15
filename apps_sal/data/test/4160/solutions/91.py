# 預金額 = 元金 + 元金 * 利子

# 将来価値
X = int(input())

# 現在価値
pv = 100

# 収益率
r = 0.01

# 必要年数
year = 0

while pv < X:
    pv = pv + pv // 100
    year += 1

print(year)

