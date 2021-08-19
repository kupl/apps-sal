def main():
    from sys import stdin, stdout
    (n, m, op) = list(map(int, stdin.readline().split()))
    hor = dict()
    vert = dict()
    for i in range(op):
        (a, b, c) = list(map(int, input().split()))
        b -= 1
        if a == 1:
            hor[b] = (c, i)
        else:
            vert[b] = (c, i)
    for i in range(n):
        for j in range(m):
            if i not in hor:
                hor[i] = (0, -1)
            if j not in vert:
                vert[j] = (0, -1)
            if hor[i][1] > vert[j][1]:
                stdout.write(str(hor[i][0]) + ' ')
            else:
                stdout.write(str(vert[j][0]) + ' ')
        stdout.write('\n')


main()
