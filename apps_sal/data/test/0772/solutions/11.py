arr = []
for i in range(3):
    arr.append([int(x) % 2 for x in input().split()])
ans = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
for i in range(3):
    for j in range(3):
        cnt = 0
        visit = [[i, j], [i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
        for x, y in visit:
            if x < 0 or y < 0 or x > 2 or y > 2:
                continue
            cnt += arr[x][y]
        if cnt % 2:
            ans[i][j] = 0
print('\n'.join(''.join(str(x) for x in l) for l in ans))
