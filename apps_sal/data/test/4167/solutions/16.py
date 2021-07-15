import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = list(map(int, readline().split()))

    ans = pow(N // K, 3)
    if K % 2 == 0 and N >= K // 2:
        ans += pow((N - K // 2) // K + 1, 3)

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
