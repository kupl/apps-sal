h, w = map(int, input().split())

s = []
for i in range(h):
    s.append('.' + input() + '.')

s = ['.' * (w + 2)] + s + ['.' * (w + 2)]

ans = 'Yes'

for i in range(1, h):
    for j in range(1, w):
        if s[i][j] == '#':
            u = s[i - 1][j]
            d = s[i + 1][j]
            l = s[i][j - 1]
            r = s[i][j + 1]
            if u == '.' and d == '.' and l == '.' and r == '.':
                ans = 'No'

print(ans)
