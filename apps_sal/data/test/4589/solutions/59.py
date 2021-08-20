(h, w) = list(map(int, input().split()))
s = [input() for i in range(h)]
ss = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
for j in range(w):
    for i in range(h):
        ss[i + 1][j + 1] = s[i][j]
s = [[0 for _ in range(w)] for _ in range(h)]
for j in range(1, w + 1):
    for i in range(1, h + 1):
        for a in range(-1, 2):
            for b in range(-1, 2):
                if a == 0 and b == 0:
                    continue
                if ss[i + a][j + b] == '#':
                    s[i - 1][j - 1] += 1
for j in range(w):
    for i in range(h):
        if ss[i + 1][j + 1] == '#':
            s[i][j] = '#'
for (i, d) in enumerate(s):
    d = list(map(str, d))
    print(''.join(d))
