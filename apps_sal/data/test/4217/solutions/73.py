import sys

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    KA = [[int(x) for x in input().split()] for _ in range(N)]

    ans = [0] * M

    for ka in KA:
        for a in ka[1:]:
            ans[a - 1] += 1

    print((sum([int(x == N) for x in ans])))


def __starting_point():
    main()


__starting_point()
