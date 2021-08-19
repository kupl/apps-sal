(h, w) = map(int, input().split())
s = ['.' * (w + 2)]
for i in range(h):
    s.append('.' + input() + '.')
s.append('.' * (w + 2))
d = [-1, 0, 1]
for i in range(1, h + 1):
    new = ''
    for j in range(1, w + 1):
        if s[i][j] == '#':
            new = new + '#'
        else:
            count = 0
            for k in range(3):
                for l in range(3):
                    if s[i + d[k]][j + d[l]] == '#':
                        count += 1
            new = new + str(count)
    print(new)
