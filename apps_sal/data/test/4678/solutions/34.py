import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)
MOD = 10 ** 9 + 7
INF = float('inf')


def main():
    N = int(input())
    A = list(map(int, input().split()))
    answer = 0
    last = A[0]
    for i in range(1, N):
        if A[i] >= last:
            last = A[i]
        else:
            answer += last - A[i]
    print(answer)


def __starting_point():
    main()


__starting_point()
