from collections import deque


def check_empty(deque_array):
    count = 0
    for q in deque_array:
        count += len(q)
    return count == 0


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end='')
        print()
    print()


def main():
    (n, m, p) = map(int, input().split())
    s = list(map(int, input().split()))
    grid = [list(input()) for _ in range(n)]
    deque_array = [deque() for _ in range(p)]
    for i in range(n):
        for j in range(m):
            if '1' <= grid[i][j] <= '9':
                x = int(grid[i][j])
                deque_array[x - 1].append((i, j, 0))
    curr_round = 1
    while not check_empty(deque_array):
        for r in range(p):
            while deque_array[r]:
                (x, y, step) = deque_array[r].popleft()
                if step >= s[r] * curr_round:
                    deque_array[r].appendleft((x, y, step))
                    break
                for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    (nx, ny) = (x + dx, y + dy)
                    if nx < 0 or nx >= n or ny < 0 or (ny >= m) or (grid[nx][ny] != '.'):
                        continue
                    grid[nx][ny] = str(r + 1)
                    deque_array[r].append((nx, ny, step + 1))
        curr_round += 1
    cell_count = [0] * p
    for i in range(n):
        for j in range(m):
            if '1' <= grid[i][j] <= '9':
                x = int(grid[i][j])
                cell_count[x - 1] += 1
    for r in range(p):
        print(cell_count[r], end=' ')
    print()


def __starting_point():
    main()


__starting_point()
