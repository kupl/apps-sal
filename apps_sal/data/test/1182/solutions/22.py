(string, column, cnt, mincnt) = map(int, input().split())
maps = [['*' for i in range(column)] for j in range(string)]
for i in range(cnt):
    (a, b) = map(int, input().split())
    maps[a - 1][b - 1] = '#'
ans = 0
for i in range(string):
    for j in range(column):
        for i1 in range(i, string):
            for j1 in range(j, column):
                num = 0
                for s in range(i, i1 + 1):
                    for c in range(j, j1 + 1):
                        if maps[s][c] == '#':
                            num += 1
                if num >= mincnt:
                    ans += 1
print(ans)
