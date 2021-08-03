def difference(ln, k, l):
    count = 0

    line2 = ln[:]
    line2[k], line2[l] = ln[l], ln[k]
    for i in range(len(ln)):
        if line2[i] != i + 1:
            count += 1

    return count


def difference2(ln):
    count = 0
    for i in range(len(ln)):
        if ln[i] != i + 1:
            count += 1

    return count


def __starting_point():

    n, m = input().split(' ')
    n = int(n)
    m = int(m)

    matrix = []
    for i in range(n):
        line = [int(i) for i in input().split(' ')]
        matrix.append(line)

    res = False

    ans = True
    for line in matrix:
        if difference2(line) > 2:
            ans = False
    if ans:
        res = True

    for i in range(m):
        for j in range(m):
            if i == j:
                continue

            answer = True
            for line in matrix:
                if difference(line, i, j) > 2:
                    answer = False

            if answer == True:
                res = True

    if res:
        print('YES')
    else:
        print('NO')


__starting_point()
