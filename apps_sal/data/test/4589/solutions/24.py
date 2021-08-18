h, w = map(int, input().split())

s = [['.'] * (w + 2)] + [list('.' + input() + '.') for i in range(h)] + [['.'] * (w + 2)]
a = [[0] * w for i in range(h)]


for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '
            a[i - 1][j - 1] = '
        else:
            b = [s[i - 1][j - 1], s[i - 1][j], s[i - 1][j + 1], s[i][j - 1], s[i][j + 1], s[i + 1][j - 1], s[i + 1][j], s[i + 1][j + 1]]
            c = b.count('

            a[i - 1][j - 1]=c

for i in range(h):
    a[i]=[str(x) for x in a[i]]
    print(''.join(a[i]))
