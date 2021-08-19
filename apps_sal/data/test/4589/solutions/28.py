(h, w) = map(int, input().split())
l = [[] for _ in range(h + 2)]
l[0] = list('.' * (w + 2))
l[h + 1] = list('.' * (w + 2))
for i in range(1, h + 1):
    l[i] = list('.' + input() + '.')
for j in range(1, h + 1):
    for k in range(1, w + 1):
        c = []
        if l[j][k] == '.':
            c += [l[j - 1][k - 1], l[j - 1][k], l[j - 1][k + 1], l[j][k - 1], l[j][k + 1], l[j + 1][k - 1], l[j + 1][k], l[j + 1][k + 1]]
            l[j][k] = str(c.count('#'))
for i in range(1, h + 1):
    ln = l[i][1:w + 1]
    s = ''.join(ln)
    print(s)
