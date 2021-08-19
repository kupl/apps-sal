from typing import List, Tuple, Set


def find_neighbors(x: int, y: int, m: int, n: int) -> List[Tuple[int, int]]:
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [p for p in neighbors if 0 <= p[0] < n and 0 <= p[1] < m]


def dfs(n: int, m: int, maze: List[List[str]], start: Tuple[int, int], max_path_length: int) -> Set[Tuple[int, int]]:
    visited = [[0] * m for _ in range(n)]
    d = [start]
    path = set()
    while d:
        (x, y) = d.pop()
        visited[x][y] = 1
        path.add((x, y))
        for (xo, yo) in find_neighbors(x, y, m, n):
            if not visited[xo][yo] and maze[xo][yo] == '.':
                d.append((xo, yo))
        if len(path) == max_path_length:
            break
    return path


def place_blocks(n: int, m: int, k: int, maze: List[List[str]], path: Set[Tuple[int, int]]) -> List[List[str]]:
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '.' and k > 0 and ((i, j) not in path):
                maze[i][j] = 'X'
                k -= 1
            if k == 0:
                return maze


def solve(n: int, m: int, k: int, maze: List[List[str]]) -> List[List[str]]:
    empty_cell_count = sum((row.count('.') for row in maze))
    for i in range(n):
        for j in range(m):
            if maze[i][j] != '#':
                path = dfs(n, m, maze, (i, j), empty_cell_count - k)
                if len(path) >= empty_cell_count - k:
                    return place_blocks(n, m, k, maze, path)


(n, m, k) = list(map(int, input().split()))
maze = [list(input()) for _ in range(n)]
for line in solve(n, m, k, maze):
    print(''.join(line))
