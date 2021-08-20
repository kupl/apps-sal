(h, w) = list(map(int, input().split()))
table = []
for i in range(h):
    line = input()
    table.append(line)
for i in range(h):
    line = ''
    for j in range(w):
        hs = max(0, i - 1)
        he = min(h - 1, i + 1)
        ws = max(0, j - 1)
        we = min(w - 1, j + 1)
        counter = 0
        for hi in range(hs, he + 1):
            for wi in range(ws, we + 1):
                if table[hi][wi] == '#':
                    counter += 1
        if table[i][j] == '#':
            line += '#'
        else:
            line += str(counter)
    print(line)
