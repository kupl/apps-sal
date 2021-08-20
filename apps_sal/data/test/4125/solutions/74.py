def resolve():
    from math import gcd
    (_, X) = [int(i) for i in input().split()]
    xx = [int(i) for i in input().split()]
    ans = abs(X - xx[0])
    for x in xx:
        ans = gcd(ans, abs(X - x))
    print(ans)


def __starting_point():
    resolve()


__starting_point()
