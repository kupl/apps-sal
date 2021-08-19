h, w = map(int, input().split())
s = []
t = []
for i in range(h):
    s.append(input())

for i in range(h):
    t.append([])
    for j in range(w):
        mines = 0
        if s[i][j] == '.':
            if i > 0 and j > 0:
                if s[i - 1][j - 1] == '#':
                    mines += 1
            if i < h - 1 and j > 0:
                if s[i + 1][j - 1] == '#':
                    mines += 1
            if i > 0 and j < w - 1:
                if s[i - 1][j + 1] == '#':
                    mines += 1
            if i < h - 1 and j < w - 1:
                if s[i + 1][j + 1] == '#':
                    mines += 1
            if i > 0:
                if s[i - 1][j] == '#':
                    mines += 1
            if i < h - 1:
                if s[i + 1][j] == '#':
                    mines += 1
            if j > 0:
                if s[i][j - 1] == '#':
                    mines += 1
            if j < w - 1:
                if s[i][j + 1] == '#':
                    mines += 1
            t[i].append(str(mines))
        else:
            t[i].append('#')

for i in range(len(t)):
    print(''.join(t[i]))
