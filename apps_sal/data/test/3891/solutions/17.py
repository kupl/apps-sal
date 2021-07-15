n, m = map(int, input().split())
a = [list(input()) for i in range(n)]
start = 0
finish = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 'B':
            finish = [i, j]
            if start == 0:
                start = finish.copy()
print((start[0] + finish[0]) // 2 + 1, (start[1] + finish[1]) // 2 + 1)
