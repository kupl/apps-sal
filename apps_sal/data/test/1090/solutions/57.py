import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = list(map(int, readline().split()))
    S = readline().strip()

    ans = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            ans += 1

    ans += 2 * K
    if ans > N - 1:
        ans = N - 1

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
