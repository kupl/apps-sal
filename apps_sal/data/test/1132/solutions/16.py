def main():
    n, m = list(map(int, input().split()))
    types = ['bus', 'ring', 'star', 'unknown']

    occ = [0] * n
    for i in range(m):
        a, b = list(map(int, input().split()))
        occ[a - 1] += 1
        occ[b - 1] += 1

    cnt = [0] * 3
    for v in occ:
        cnt[min(2, v - 1)] += 1

    if cnt == [2, n - 2, 0]:
        res = types[0]
    elif cnt == [0, n, 0]:
        res = types[1]
    elif cnt == [n - 1, 0, 1]:
        res = types[2]
    else:
        res = types[3]

    print(res, 'topology')


def __starting_point():
    main()


__starting_point()
