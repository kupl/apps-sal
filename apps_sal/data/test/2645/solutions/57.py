import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    g, p = 0, 0
    ans = 0
    for c in S:
        if g > p:
            p += 1
            if c == 'g':
                ans += 1
        else:
            g += 1
            if c == 'p':
                ans -= 1

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
