(h, w) = map(int, input().split())
s = []
for _ in range(h):
    s.append(list(input()))
for i in range(h):
    for j in range(w):
        a = 0
        if s[i][j] == '.':
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if (0 <= k and k <= h - 1) and (0 <= l and l <= w - 1) and (s[k][l] == '#'):
                        a += 1
            s[i][j] = str(a)
for m in range(h):
    print(''.join(s[m]))
