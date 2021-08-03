import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] %= MOD
    S = sum(A)
    answer = 0
    for i in range(N):
        S = S - A[i]
        answer += A[i] * S
        answer %= MOD
    print(answer)


def __starting_point():
    main()


__starting_point()
