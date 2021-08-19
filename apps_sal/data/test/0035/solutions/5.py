def matrixTranspose(matrix):
    if not matrix:
        return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def f(x):
    bool = True
    (b, r, g) = (0, 0, 0)
    col = ['e']
    for row in x:
        if all((el == 'R' for el in row)):
            r += 1
            if col[-1] != 'r':
                col.append('r')
        elif all((el == 'G' for el in row)):
            g += 1
            if col[-1] != 'g':
                col.append('g')
        elif all((el == 'B' for el in row)):
            b += 1
            if col[-1] != 'b':
                col.append('b')
        else:
            bool = False
            break
    return bool and b == g == r and (sorted(col) == sorted(list(set(col))))


(n, m) = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = list(input())
print('YES' if f(a) or f(matrixTranspose(a)) else 'NO')
