import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, *A) = list(map(int, read().split()))
    K = len(set(A))
    if K % 2 == 1:
        ans = K
    else:
        ans = K - 1
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
