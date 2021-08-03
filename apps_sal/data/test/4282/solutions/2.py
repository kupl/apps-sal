def read_nums():
    return [int(x) for x in input().split()]


def main():
    n, = read_nums()
    d = {}
    for i in range(1, n + 1):
        d[i] = read_nums()

    circle = {1: d[1][0] if d[1][1] in d[d[1][0]] else d[1][1]}

    prev = 1
    cur = circle[1]
    while cur != 1:
        circle[cur] = list(set(d[prev]) & set(d[cur]))[0]
        prev = cur
        cur = circle[cur]

    nums = [1]
    cur = circle[1]
    while cur != 1:
        nums.append(cur)
        cur = circle[cur]
    print(' '.join([str(x) for x in nums]))


def __starting_point():
    main()


__starting_point()
