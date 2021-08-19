def check(a, b, m, n):
    for i in range(m):
        for j in range(n):
            k = 0
            for x in range(m):
                k |= a[x][j]
            for x in range(n):
                k |= a[i][x]
            if k != b[i][j]:
                return False
    return True


def input_values():
    return [int(x) for x in input().split()]


(m, n) = input_values()
b = []
for i in range(m):
    b.append(input_values())
a = [[1 for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        if b[i][j] == 0:
            for x in range(m):
                a[x][j] = 0
            for x in range(n):
                a[i][x] = 0
if check(a, b, m, n):
    print('YES')
    for i in range(m):
        print(' '.join([str(x) for x in a[i]]))
else:
    print('NO')
