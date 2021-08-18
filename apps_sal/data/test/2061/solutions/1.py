
from collections import deque


def main():
    DELTAS = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    )

    try:
        while True:
            n, m, k = list(map(int, input().split()))
            grid = [list(input()) for i in range(n)]
            lakes = []
            q = deque()
            for i in range(n):
                for j in (0, m - 1):
                    if grid[i][j] == '.':
                        grid[i][j] = '?'
                        q.append((i, j))
                        while q:
                            y, x = q[0]
                            q.popleft()
                            for dy, dx in DELTAS:
                                ny = y + dy
                                nx = x + dx
                                if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == '.':
                                    grid[ny][nx] = '?'
                                    q.append((ny, nx))
            for i in (0, n - 1):
                for j in range(m):
                    if grid[i][j] == '.':
                        grid[i][j] = '?'
                        q.append((i, j))
                        while q:
                            y, x = q[0]
                            q.popleft()
                            for dy, dx in DELTAS:
                                ny = y + dy
                                nx = x + dx
                                if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == '.':
                                    grid[ny][nx] = '?'
                                    q.append((ny, nx))
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == '.':
                        grid[i][j] = '?'
                        q.append((i, j))
                        area = 1
                        while q:
                            y, x = q[0]
                            q.popleft()
                            for dy, dx in DELTAS:
                                ny = y + dy
                                nx = x + dx
                                if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == '.':
                                    grid[ny][nx] = '?'
                                    q.append((ny, nx))
                                    area += 1

                        lakes.append((area, i, j))

            lakes.sort(reverse=True)
            print(sum(x[0] for x in lakes[k:]))
            for _, i, j in lakes[k:]:
                grid[i][j] = '*'
                q.append((i, j))
                while q:
                    y, x = q[0]
                    q.popleft()
                    for dy, dx in DELTAS:
                        ny = y + dy
                        nx = x + dx
                        if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == '?':
                            grid[ny][nx] = '*'
                            q.append((ny, nx))

            print('\n'.join("".join(ls).replace('?', '.') for ls in grid))

    except EOFError:
        pass


main()
