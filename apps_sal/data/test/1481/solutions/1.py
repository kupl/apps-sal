N = int(input())
m = [input() for i in range(N)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for x in range(N):
    for y in range(N):
        cnt = 0
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < N and m[ty][tx] == 'o':
                cnt += 1
        if cnt % 2:
            print('NO')
            return
print('YES')
