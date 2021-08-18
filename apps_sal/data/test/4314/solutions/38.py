import numpy as np

h, w = map(int, input().split())

maze = []
for i in range(h):
    row = list(input())
    if "
    maze.append(row)

maze = np.array(maze)
maze = np.rot90(maze)

ans = []
for row in maze:
    if "
    ans.append(row)

ans = np.rot90(ans, -1)

for r in ans:
    print("".join(r))
