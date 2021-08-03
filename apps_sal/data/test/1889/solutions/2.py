import math


def linescore(line):
    acc = 0
    ret = 0
    for eye in line:
        if eye:
            acc += 1
            ret = max(ret, acc)
        else:
            acc = 0
    return ret


def main():
    items = input().split()
    n = int(items[0])
    m = int(items[1])
    q = int(items[2])
    e = [[None for _ in range(m)] for _ in range(n)]
    ls = [0 for _ in range(n)]
    for i in range(n):
        items = input().split()
        for j in range(m):
            e[i][j] = (items[j] == '1')
    for i in range(n):
        ls[i] = linescore(e[i])
    for qi in range(q):
        items = input().split()
        x = int(items[0]) - 1
        y = int(items[1]) - 1
        e[x][y] = not e[x][y]
        ls[x] = linescore(e[x])
        print(max(ls))


def __starting_point():
    main()


__starting_point()
