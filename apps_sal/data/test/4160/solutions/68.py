# 1年後 m1 = 100 * 1.01
# 2年後 m2 = m1 * 1.01
# 3年後 m3 = m2 * 1.01

x = int(input())
m = 100
y = 0
while m < x:
    m += m // 100
    y += 1
print(y)
