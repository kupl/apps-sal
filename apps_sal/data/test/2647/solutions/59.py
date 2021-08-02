#!/usr/bin/env python
# coding: utf-8

# In[47]:


from collections import deque


# In[50]:


H, W = list(map(int, input().split()))
grid = [list("#" * (W + 2))]
b_cnt = 0
for _ in range(H):
    tmp = list(input())
    grid.append(["#"] + tmp + ["#"])
grid.append(list("#" * (W + 2)))


# In[52]:


grid[1][1] = 1
q = deque([[1, 1]])
move = [
    [1, 0], [-1, 0], [0, 1], [0, -1]
]
while q:
    x, y = q.popleft()
    for dx, dy in move:
        if grid[x + dx][y + dy] == ".":
            grid[x + dx][y + dy] = grid[x][y] + 1
            q.append([x + dx, y + dy])
if grid[H][W] == ".":
    print((-1))
else:
    print(((H + 2) * (W + 2) - sum(g.count("#") for g in grid) - grid[H][W]))


# In[ ]:
