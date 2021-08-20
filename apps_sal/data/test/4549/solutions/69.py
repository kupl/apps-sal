(h, w) = map(int, input().split())
s = []
s.append(['.'] * (w + 2))
for i in range(h):
    s.append([a for a in input()])
    s[i + 1].insert(0, '.')
    s[i + 1].append('.')
s.append(['.'] * (w + 2))
check = True
for j in range(1, h + 1):
    for k in range(1, w + 1):
        if s[j][k] == '#':
            if s[j + 1][k] == '.' and s[j - 1][k] == '.' and (s[j][k + 1] == '.') and (s[j][k - 1] == '.'):
                check = False
print('Yes' if check else 'No')
