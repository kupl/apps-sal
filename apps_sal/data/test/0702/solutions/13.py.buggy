n = int(input())
arr = [[x for x in input()] for _ in range(n)]
move = [(1, -1), (1, 0), (1, 1), (2, 0)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == '.':
            arr[i][j] = '#'
            for m in move:
                mi, mj = i + m[0], j + m[1]
                if 0 <= mi < n and 0 <= mj < n and arr[mi][mj] == '.':
                    arr[mi][mj] = '#'
                else:
                    print('NO')
                    return
print('YES')
