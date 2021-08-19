def lcm(a, b):
    """最小公倍数"""
    from math import gcd
    return a * b // gcd(a, b)


def solve(N, M, As):
    if sum([a % 2 for a in As]) > 0:
        print(0)
        return
    As = [a // 2 for a in As]
    all_lcm = 1
    for a in As:
        all_lcm = lcm(all_lcm, a)
        if all_lcm > M:
            print(0)
            return
    for a in As:
        if all_lcm // a % 2 == 0:
            print(0)
            return
    from math import ceil
    print(ceil(M // all_lcm / 2))


def __starting_point():
    (N, M) = list(map(int, input().split()))
    As = [int(i) for i in input().split()]
    solve(N, M, As)


__starting_point()
