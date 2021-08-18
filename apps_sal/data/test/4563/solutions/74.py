
import sys
import math


def main():
    mod = 1000000007
    inf = float('inf')
    sys.setrecursionlimit(10**6)
    def input(): return sys.stdin.readline().rstrip()
    def ii(): return int(input())
    def mi(): return list(map(int, input().split()))
    def mi_0(): return [int(x) - 1 for x in input().split()]
    def lmi(): return list(map(int, input().split()))
    def lmi_0(): return list([int(x) - 1 for x in input().split()])
    def li(): return list(input())

    def calc_minimum_card_pair(a, b, s, t):
        """
        現在 a, b 枚であるとする
        カードを増やす操作を行い比を s : t にするとき、変化後のカード枚数を返す
        """
        multiply_rate = max((a + s - 1) // s, (b + t - 1) // t)
        return (s * multiply_rate, t * multiply_rate)

    n = ii()
    L = [lmi() for _ in range(n)]
    a, b = 1, 1
    for s, t in L:
        a, b = calc_minimum_card_pair(a, b, s, t)

    print((a + b))


def __starting_point():
    main()


__starting_point()
