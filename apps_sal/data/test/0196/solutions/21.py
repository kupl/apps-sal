def powermod(base, power):
    if power == 0:
        return 1
    if power == 1:
        return base
    ret = powermod(base, power // 2)
    ret *= ret
    ret %= 1000000007
    if power % 2 == 1:
        ret *= base
        ret %= 1000000007
    return ret


x, k = list(map(int, input().split()))

b = x * 2 - 1
ans = b * powermod(2, k) + 1
ans %= 1000000007

if x == 0:
    ans = 0
print(ans)
