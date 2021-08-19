from collections import Counter
from functools import reduce


def main():
    input()
    MOD = int(1000000000.0 + 7)
    u = list(map(int, input().split()))
    v = Counter(u)
    e = reduce(lambda a, b: a * b, [it + 1 for it in list(v.values())])
    ans = 1
    e %= 2 * (MOD - 1)
    for (a, b) in list(v.items()):
        ans = ans * pow(a, b * e // 2, MOD) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
