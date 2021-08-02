import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = list(map(int, readline().split()))

    ans = 0
    step = K if K % 2 else K // 2

    for a in range(step, N + 1, step):
        l = a // K + 1
        r = (N + a) // K
        if r >= l:
            ans += (r - l + 1) ** 2

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
