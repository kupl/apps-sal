MOD = 1000 * 1000 * 1000 + 7


def pow(x, e, m):
    res = 1
    x = x % m

    while e > 0:
        if(e % 2 == 1):
            res = (res * x) % m

        e = e // 2
        x = (x * x) % m

    return res


x, k = map(int, input().split(' '))


if x == 0:
    print(0)

else:
    myres = (pow(2, k, MOD) * (2 * x - 1) + 1) % MOD
    print(myres)
