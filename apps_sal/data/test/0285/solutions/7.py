def cross(l1, l2, x2):
    return l2[0] * x2 + l2[1] < l1[0] * x2 + l1[1]


def __starting_point():
    n = int(input())
    x1, x2 = list(map(int, input().split()))
    data = [tuple(map(int, input().split())) for i in range(n)]

    data = list(sorted(data, key=lambda x: (x[0] * x1 + x[1], x[0] * x2 + x[1])))
    for i in range(len(data) - 1):
        if cross(data[i], data[i + 1], x2):
            print('YES')
            return

    print('NO')


__starting_point()
