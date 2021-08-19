from itertools import accumulate
import sys
read = sys.stdin.read


def main():
    maxa2 = 10 ** 5 + 1
    maxa2 = max(6, maxa2)
    p = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(maxa2)]
    p[0] = p[1] = False
    p[2] = p[3] = p[5] = True
    for is1 in range(3, maxa2, 2):
        for is2 in range(is1 ** 2, maxa2, is1):
            p[is2] = False
    prime_list = [i for (i, b) in enumerate(p) if b]
    p2017 = [0] * (10 ** 5 * 2 + 1)
    for pr in prime_list:
        if p[(pr + 1) // 2]:
            p2017[pr] = True
    p2017a = tuple(accumulate(p2017))
    q = int(input())
    m = map(int, read().split())
    for (l, r) in zip(m, m):
        print(p2017a[r] - p2017a[l - 1])


def __starting_point():
    main()


__starting_point()
