from collections import deque

dic = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
[n, m], hor, vert = list(map(int, input().split())), input().strip(), input().strip()
for _x in range(n):
    for _y in range(m):
        q, d = deque([(_x, _y)]), [[0] * m for x in range(n)]
        d[_x][_y] = 1
        while q:
            x, y = q.popleft()
            for direction in '><v^':
                dx, dy = dic[direction]
                if -1 < x + dx < n and -1 < y + dy < m and (vert[y] == direction if dx else hor[x] == direction) and not d[x + dx][y + dy]:
                    d[x + dx][y + dy] = 1
                    q.append((x + dx, y + dy))
        if sum(sum(d, [])) != n * m:
            print('NO')
            break
    else:
        continue
    break
else:
    print('YES')

