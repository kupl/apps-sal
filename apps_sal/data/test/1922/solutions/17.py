n, m = map(int, input().split())
ret = 0
if (n == 1) and (m == 1):
    # 点
    ret = 1
elif (n == 1) or (m == 1):
    # 線
    ret = n * m - 2
else:
    # 面
    ret = m * n - m * 2 - n * 2 + 4
print(ret)
