import sys


def check(x):
    (t, p) = (0, 0)
    for i in range(5):
        if x[i] == 'X':
            t += 1
        elif x[i] == '.':
            p += 1
    if t == 4 and p == 1:
        return True
    return False


def main():
    x = []
    for i in range(10):
        x.append(sys.stdin.readline().rstrip())
    flag = False
    for i in range(10):
        for j in range(10):
            if j + 4 < 10 and check([x[i][k] for k in range(j, j + 5)]):
                flag = True
            if i + 4 < 10 and check([x[k][j] for k in range(i, i + 5)]):
                flag = True
            if i + 4 < 10 and j + 4 < 10 and check([x[i + k][j + k] for k in range(5)]):
                flag = True
            if i + 4 < 10 and j - 4 >= 0 and check([x[i + k][j - k] for k in range(5)]):
                flag = True
    if flag:
        print('YES')
    else:
        print('NO')


main()
