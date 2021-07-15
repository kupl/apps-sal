import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    ans1 = ans2 = 0
    for i, c in enumerate(S):
        if i % 2 == int(c):
            ans1 += 1
        else:
            ans2 += 1

    print((min(ans1, ans2)))
    return


def __starting_point():
    main()

__starting_point()
