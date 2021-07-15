h, w = map(int, input().split())
T = [[] for i in range(h)]
num = 0
for i in range(h):
    T[i] = list(input())
    for j in range(w):
        if T[i][j] == '*':
            num += 1
if num >= h + w:
    print('NO')
    return
for i in range(h):
    for j in range(w):
        if T[i][j] == '*':
            tmp = 1
            x, y = i, j
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < h and 0 <= ny < w and T[nx][ny] == '*'):
                    tmp = -1000000
                    break
                while 0 <= nx < h and 0 <= ny < w and T[nx][ny] == '*':
                    tmp += 1
                    nx, ny = nx + dx, ny + dy

            if tmp == num:
                print('YES')
                return

print('NO')
