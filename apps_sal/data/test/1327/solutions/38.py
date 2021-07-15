import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)
MOD = 10 ** 9 + 7


def main():
    N, M = list(map(int, input().split()))
    cake = [list(map(int, input().split())) for _ in range(N)]
    C = [[] for _ in range(8)]
    for i in range(2 ** 3):
        for c in range(N):
            m = 0
            for j in range(3):
                if (i >> j) & 1:
                    m += cake[c][j]
                else:
                    m -= cake[c][j]
            C[i].append(m)
    answer = 0
    for i in range(8):
        C[i].sort(reverse=True)
        ans = sum(C[i][:M])
        if ans > answer:
            answer = ans
    print(answer)


def __starting_point():
    main()

__starting_point()
