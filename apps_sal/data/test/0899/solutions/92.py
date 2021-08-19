import sys
input = sys.stdin.readline


def main():
    (n, m) = map(int, input().split())
    road = [[100000] * n for _ in range(n)]
    count = [[-1] * n for i in range(n)]
    for _ in range(m):
        (a, b, c) = map(int, input().split())
        road[a - 1][b - 1] = c
        road[b - 1][a - 1] = c
        count[a - 1][b - 1] = 0
        count[b - 1][a - 1] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if road[i][k] + road[k][j] < road[i][j]:
                    if count[i][j] == 0:
                        count[i][j] = 1
                    road[i][j] = road[i][k] + road[k][j]
    ans = 0
    for i in range(n):
        ans += count[i].count(1)
    print(ans // 2)


def __starting_point():
    main()


__starting_point()
