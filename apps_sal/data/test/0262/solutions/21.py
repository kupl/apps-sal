def main():
    n = int(input())
    matrix = []
    s = None
    found = False
    col = 0
    row = 0
    if n == 1:
        i = input()
        return 1
    for i in range(n):
        line = [int(k) for k in input().split(' ')]
        matrix.append(line)
        if not found:
            try:
                index = line.index(0)
                row = i
                col = index
                continue
            except ValueError:
                pass
        if s is None:
            s = sum(line)
        elif s != sum(line):
            return -1
    res = s - sum(matrix[row])
    if res < 1:
        return -1
    else:
        matrix[row][col] = res
    for i in range(n):
        t = 0
        for j in range(n):
            t += matrix[j][i]
        if t != s:
            return -1
    d1 = 0
    d2 = 0
    for i in range(n):
        d1 += matrix[i][i]
        d2 += matrix[i][n - 1 - i]
    if d1 != s or d2 != s:
        return -1
    return res


def __starting_point():
    print(main())


__starting_point()
