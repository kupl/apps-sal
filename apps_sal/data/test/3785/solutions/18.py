from sys import stdin
from collections import deque

def __starting_point():
    R, C, K = list(map(int, stdin.readline().rstrip().split()))
    maze = []
    start = None
    for r in range(0, R):
        line = stdin.readline()
        if start is None:
            for c in range(0, C):
                if line[c] == '.':
                    start = (r, c)
                    break
        maze.append(list(line))

    order = deque()
    stack = deque()
    stack.append(start)

    def add_to_stack(row, col):
        if 0 <= row < R and \
                0 <= col < C and \
                maze[row][col] == '.':
            stack.append((row, col))
            maze[row][col] = ','

    while len(stack) > 0:
        (r, c) = stack.pop()
        order.append((r, c))
        add_to_stack(r-1, c)
        add_to_stack(r+1, c)
        add_to_stack(r, c-1)
        add_to_stack(r, c+1)

    for k in range(0, K):
        (r, c) = order.pop()
        maze[r][c] = 'X'

    for r in range(0, R):
        line = ''
        for c in range(0, C):
            ch = maze[r][c]
            if ch == ',':
                line += '.'
            else:
                line += ch
        print(line)


__starting_point()
