n, x = list(map(int, input().split()))

p = [0] * -~n
l = [0] * -~n

p[0] = 1
l[0] = 1
for i in range(1, n + 1):
    p[i] = p[i - 1] * 2 + 1
    l[i] = l[i - 1] * 2 + 3

# バーガーの長さは奇数


def rec(m, y):
    if y == 0:
        return 0
    if m == 0:
        return 1
    h = l[m] // 2  # レベルmの半分より左側の長さ
    if h < y:  # 真ん中含む
        return 1 + p[m - 1] + rec(m - 1, y - h - 1)
    else:
        return rec(m - 1, y - 1)


print((rec(n, x)))

