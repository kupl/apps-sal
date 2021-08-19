from collections import defaultdict, deque


def main():
    (n, m) = map(int, input().split())
    a = [[c for c in input()] for i in range(n)]
    che = [[0 for i in range(n + 2)] for j in range(n + 2)]
    ans = 0
    for j in range(m):
        check = False
        for i in range(n - 1):
            if a[i][j] > a[i + 1][j]:
                if not che[i][i + 1]:
                    ans += 1
                    check = True
                    break
        if not check:
            for i in range(n - 1):
                if a[i][j] < a[i + 1][j]:
                    che[i][i + 1] = 1
    print(ans)


def __starting_point():
    main()


__starting_point()
