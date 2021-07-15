h, w = list(map(int, input().split()))
s = ['.' + input() + '.' for _ in range(h)]
s = ['.' * (w + 2)] + s + ['.' * (w + 2)]

for y in range(1, h + 1):
    for x in range(1, w + 1):
        if s[y][x] == '#' and all(s[y + dy][x + dx] == '.' for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]):
            print('No')
            return
print('Yes')

