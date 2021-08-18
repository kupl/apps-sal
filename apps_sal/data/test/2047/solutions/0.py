import sys


def main():
    f = sys.stdin
    n = int(f.readline())
    b = list(map(int, f.readline().strip().split(' ')))
    a = list(map(int, f.readline().strip().split(' ')))
    b = [b[i] - a[i] for i in range(n)]
    c = [[0, 0]]
    for i in range(n - 1):
        line = f.readline().strip().split(' ')
        c.append([int(line[0]), int(line[1])])
    for i in range(n - 1, 0, -1):
        fa = c[i][0] - 1
        if b[i] >= 0:
            b[fa] += b[i]
        else:
            b[fa] += b[i] * c[i][1]
            if b[fa] < -1e17:
                print('NO')
                return 0
    if b[0] >= 0:
        print('YES')
    else:
        print('NO')


main()
