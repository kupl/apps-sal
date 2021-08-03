import itertools
import sys


def main():
    input = sys.stdin.readline
    n, m, r = map(int, input().split())
    R = [int(x) for x in input().split()]
    inf = pow(10, 9) + 7

    roads = [[inf] * n for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        roads[a - 1][b - 1] = c
        roads[b - 1][a - 1] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if roads[i][j] > roads[i][k] + roads[k][j]:
                    roads[i][j] = roads[i][k] + roads[k][j]

    ans = inf
    for value in itertools.permutations(R):
        sub = 0
        for k in range(r - 1):
            sub += roads[value[k] - 1][value[k + 1] - 1]
        if ans > sub:
            ans = sub

    print(ans)


def __starting_point():
    main()


__starting_point()
