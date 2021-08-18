h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            m = 0
            if i - 1 >= 0 and j - 1 >= 0:
                if s[i - 1][j - 1] == '
                m += 1
            if i - 1 >= 0:
                if s[i - 1][j] == '
                m += 1
            if i - 1 >= 0 and j + 1 < w:
                if s[i - 1][j + 1] == '
                m += 1
            if j - 1 >= 0:
                if s[i][j - 1] == '
                m += 1
            if j + 1 < w:
                if s[i][j + 1] == '
                m += 1
            if i + 1 < h and j - 1 >= 0:
                if s[i + 1][j - 1] == '
                m += 1
            if i + 1 < h:
                if s[i + 1][j] == '
                m += 1
            if i + 1 < h and j + 1 < w:
                if s[i + 1][j + 1] == '
                m += 1
            s[i][j] = str(m)
for i in range(h):
    z = list(s[i])
    print(''.join(z))
