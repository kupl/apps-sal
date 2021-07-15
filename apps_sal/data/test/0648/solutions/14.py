def calc(x):
    y = - x // m + b
    ret = 0
    fix1 = y * (y + 1) // 2
    ret += fix1 * (x + 1)
    fix2 = x * (x + 1) // 2
    ret += fix2 * (y + 1)
    # print(x, ret)
    return ret

m, b = list(map(int, input().split()))
i = 0
ans = 0
while i <= m * b:
    ans = max(ans, calc(i))
    i += m
print(ans)

