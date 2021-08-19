from fractions import gcd


def main():
    N = int(input())
    a_list = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    a_lcm = a_list[0]
    for a in a_list[1:]:
        a_lcm *= a // gcd(a, a_lcm)
    res = 0
    for a in a_list:
        res += a_lcm // a
    print(res % MOD)


def __starting_point():
    main()


__starting_point()
