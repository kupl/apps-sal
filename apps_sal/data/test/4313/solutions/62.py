import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    V = list(map(int, readline().split()))
    C = list(map(int, readline().split()))

    ans = 0
    for v, c in zip(V, C):
        if v > c:
            ans += v - c

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
