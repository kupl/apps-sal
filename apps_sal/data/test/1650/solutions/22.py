import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    L = readline().strip()

    eq, less = 2, 1
    for d in L[1:]:
        if d == '1':
            less = (eq + 3 * less) % MOD
            eq = 2 * eq % MOD
        else:
            less = 3 * less % MOD

    print(((eq + less) % MOD))
    return


def __starting_point():
    main()


__starting_point()
