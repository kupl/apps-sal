a = [[3, 3, 4, 4, 3, 3], [3, 3, 4, 4, 3, 3], [2, 2, 3, 3, 2, 2], [2, 2, 3, 3, 2, 2], [1, 1, 2, 2, 1, 1], [1, 1, 2, 2, 1, 1]]
b = []
go = True
for i in range(6):
    b.append(input())
for x in range(4, 0, -1):
    for i in range(6):
        for j in range(6):
            if a[i][j] == x:
                if b[i][j + j // 2] == '.':
                    b[i] = b[i][:j + j // 2] + 'P' + b[i][j + j // 2 + 1:]
                    go = False
                    break
        if not go:
            break
    if not go:
        break
[print(i) for i in b]
