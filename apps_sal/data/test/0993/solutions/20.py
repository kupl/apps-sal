import sys
from collections import Counter
from itertools import accumulate


def main():
    mod = 1000000007
    inf = float('inf')
    sys.setrecursionlimit(10 ** 6)

    def input():
        return sys.stdin.readline().rstrip()

    def ii():
        return int(input())

    def mi():
        return list(map(int, input().split()))

    def mi_0():
        return [int(x) - 1 for x in input().split()]

    def lmi():
        return list(map(int, input().split()))

    def lmi_0():
        return list([int(x) - 1 for x in input().split()])

    def li():
        return list(input())
    (n, m) = mi()
    L = list([int(x) % m for x in input().split()])
    accum = [0] + list(accumulate(L, lambda x, y: (x + y) % m))
    ans = 0
    for (_, duplicate_num) in list(Counter(accum).items()):
        ans += duplicate_num * (duplicate_num - 1) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
