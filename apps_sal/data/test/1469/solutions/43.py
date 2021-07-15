# from https://atcoder.jp/contests/abc108/submissions/4342595
import math


def main():
    l = int(input())
    n = math.floor(math.log2(l)) + 1
    e = []
    for v in range(n-1):
        v2 = 2 ** v
        e.append([v + 1, v + 2, 0])
        e.append([v + 1, v + 2, v2])
        if (l >> v) & 1:
            e.append([v + 1, n, l - v2])
            l -= v2
    print((n, len(e)))
    for x in e:
        print((*x))


main()

