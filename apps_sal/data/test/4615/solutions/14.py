import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A, B, C, D, E, F = list(map(int, input().split()))

    water = set()
    for a in range(F // (A * 100) + 1):
        for b in range(F // (B * 100) + 1):
            if 0 < a * 100 * A + b * 100 * B <= F:
                water.add(a * 100 * A + b * 100 * B)

    kouho = []
    for w in water:
        ma = (E * w) // 100
        for c in range(ma // C + 1):
            for d in range(ma // D + 1):
                sugar = c * C + d * D
                if 0 < sugar <= ma and w + sugar <= F:
                    kouho.append([w, sugar])

    if len(kouho) == 0:
        print((list(water)[0], 0))
        return

    max_noudo = 0
    res = []
    for w, sugar in kouho:
        noudo = sugar / (w + sugar)
        if max_noudo < noudo:
            max_noudo = noudo
            res = [w + sugar, sugar]
    print((*res))


def __starting_point():
    resolve()

__starting_point()
