#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque


# In[2]:


H,W = list(map(int, input().split()))
S = []
for _ in range(H):
    S.append(input())


# In[3]:


def bfs(sx,sy):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    d = [[-1]*W for _ in range(H)]
    q = deque([])
    q.append([sx,sy])
    d[sx][sy] = 0
    ans = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] != "#" and d[nx][ny] == -1:
                q.append([nx,ny])
                d[nx][ny] = d[x][y] + 1
                ans = max(ans,d[nx][ny])
    return ans


# In[5]:


ans = 0
for sh in range(H):
    if "." in S[sh]:
        for sw in range(W):
            if S[sh][sw] == ".":
                ans = max(ans,bfs(sh,sw))
print(ans)


# In[ ]:





