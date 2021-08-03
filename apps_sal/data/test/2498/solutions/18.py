import copy
# from math import gcd


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return (a // gcd(a, b)) * b


def main():
    n, m = map(int, input().split())
    A = set([int(x) for x in input().split()])
    a_lcm = 1
    for a in A:
        a_lcm = lcm(a_lcm, a)
        # mがlcmの半分よりも小さかったら0
        if (a_lcm / 2) > m:
            print(0)
            return
    for a in A:
        if (a_lcm / 2) % a == 0:
            print(0)
            return
    # # あとは定数倍の数調べて終わり
    ans = int((m - (a_lcm / 2)) // a_lcm) + 1
    print(ans)


def __starting_point():
    main()


__starting_point()
