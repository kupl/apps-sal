import sys
my_file = sys.stdin
a = my_file.read().strip().split('\n')


def result():
    for i in range(3):
        for k in range(3):
            if (a[i][k] == a[i][k + 1] == a[i + 1][k] == '#' or a[i][k] == a[i][k + 1] == a[i + 1][k + 1] == '#') or (a[i][k] == a[i][k + 1] == a[i + 1][k] == '.' or a[i][k] == a[i][k + 1] == a[i + 1][k + 1] == '.') or (a[i + 1][k] == a[i + 1][k + 1] == a[i][k] == '#' or a[i + 1][k] == a[i + 1][k + 1] == a[i][k + 1] == '#') or (a[i + 1][k] == a[i + 1][k + 1] == a[i][k] == '.' or a[i + 1][k] == a[i + 1][k + 1] == a[i][k + 1] == '.'):
                print('YES')
                return
    else:
        print('NO')
        return


result()
