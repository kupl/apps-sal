(h, w) = map(int, input().split())
l = [['.'] * (w + 2)]
for i in range(h):
    l.append(['.'] + [i for i in input()] + ['.'])
l.append(['.'] * (w + 2))


def count(i, j):
    if l[i][j] == '#':
        return '#'
    c = 0
    for n in range(i - 1, i + 2):
        for m in range(j - 1, j + 2):
            if l[n][m] == '#':
                c += 1
    return str(c)


ans = [''.join([count(i, j) for j in range(1, 1 + w)]) for i in range(1, 1 + h)]
print('\n'.join(ans))
