
from collections import defaultdict


def main():
    n, m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]

    dict1 = defaultdict(list)
    for i in range(n):
        for j in range(m):
            dict1[i + j].append(a[i][j])

    dict2 = defaultdict(list)
    for i in range(n):
        for j in range(m):
            dict2[i + j].append(b[i][j])

    for i in range(n + m - 1):
        if sorted(dict1[i]) != sorted(dict2[i]):
            print('NO')
            return
    print('YES')


def __starting_point():
    main()


__starting_point()
