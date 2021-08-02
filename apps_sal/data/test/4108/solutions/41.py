import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def solve(S, T):
    d = dict()
    for s, t in zip(S, T):
        if s in d and d[s] != t:
            return False
        else:
            d[s] = t

    return True


def main():
    S = readline().strip()
    T = readline().strip()

    if solve(S, T) and solve(T, S):
        print('Yes')
    else:
        print('No')

    return


def __starting_point():
    main()


__starting_point()
