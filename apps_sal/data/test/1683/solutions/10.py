from collections import Counter

b = 998244353


def __starting_point():
    n = int(input())
    arr = input().split()
    mp = list(map(lambda x: len(x), arr))
    cnt = Counter(mp)

    s = 0
    for a in arr:
        l = list(reversed(a))
        for num, ln in cnt.items():
            l1 = int("".join(list(reversed(["%s0" % x if i < num else x for i, x in enumerate(l)]))))
            l2 = int("".join(list(reversed(["0%s" % x if j < num else x for j, x in enumerate(l)]))))
            s = (s + l1 * ln) % b
            s = (s + l2 * ln) % b

    print(s)


__starting_point()
