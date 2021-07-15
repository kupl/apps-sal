import numpy as np
H ,W = map(int,input().split())

maze = [[] for _ in range(H)]
for i in range(H):
    maze[i] = np.array(list(input())) == "."
maze = np.array(maze)

up = np.zeros((H, W), dtype=int)
down = np.zeros((H, W), dtype=int)
right = np.zeros((H, W), dtype=int)
left = np.zeros((H, W), dtype=int)

for i in range(H):
    up[i] = (up[i-1] + 1)*maze[i]
    down[-(i+1)] = (down[-i] + 1)*maze[-(i+1)] 
    
#print(up)
#print(down)

for i in range(W):
    right[:, i] = (right[:, i-1] + 1)*maze[:, i]
    left[:, -(i+1)] = (left[:, -i] + 1)*maze[:, -(i+1)]

print(np.max(up+down+right+left)-3)
