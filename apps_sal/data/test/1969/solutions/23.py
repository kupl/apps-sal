n = int(input())
T = [[] for i in range(n)]
for i in range(n):
    a = list(input())
    T[i] = a
num = 0
for i in range(n):
    for j in range(n):
        if T[i][j] == 'X':
            for (dx, dy) in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                (nx, ny) = (i + dx, j + dy)
                flag = True
                if 0 <= nx < n and 0 <= ny < n and (T[nx][ny] == 'X'):
                    continue
                else:
                    flag = False
                    break
            if flag:
                num += 1
print(num)
