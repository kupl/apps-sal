x = int(input())
# 階差数列
y, i = 1, 1
while y < x:
    i += 1
    y += i
print(i)
