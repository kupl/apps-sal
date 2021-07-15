import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    B = [0]
    B.extend(A)
    B.append(0)

    M = len(B)

    total = 0
    for i in range(M - 1):
        total += abs(B[i + 1] - B[i])

    ans = [0] * N
    for i in range(N):
        ans[i] = total - abs(B[i + 1] - B[i]) - abs(B[i + 2] - B[i + 1]) + abs(B[i + 2] - B[i])

    print(*ans, sep='\n')
    return


def __starting_point():
    main()

__starting_point()
