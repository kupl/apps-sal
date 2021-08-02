def in_int():
    return int(input())


def in_list():
    return [int(x) for x in input().split()]


n, m = in_list()
mat = []
first = -1
for i in range(n):
    mat.append(in_list())
    if first == -1:
        for j in range(m - 1):
            if mat[-1][j] != mat[-1][j + 1]:
                first = (i, j)
                break
if first == -1:
    ans = 0
    for i in range(n):
        ans = ans ^ mat[i][0]
    if ans > 0:
        print('TAK')
        print(' '.join(['1'] * n))
    else:
        print('NIE')
else:
    r, c = first
    print('TAK')
    ans = 0
    for i in range(n):
        if i != r:
            ans = ans ^ mat[i][0]
        else:
            ans = ans ^ mat[i][c]
    if ans > 0:
        for i in range(n):
            if i != r:
                print(0 + 1, end=' ')
            else:
                print(c + 1, end=' ')
    else:
        for i in range(n):
            if i != r:
                print(0 + 1, end=' ')
            else:
                print(c + 2, end=' ')
