from collections import defaultdict, deque
text = input().strip()
v = len(text)
g = defaultdict(list)
store = defaultdict(list)
for i in range(1, v):
    temp = ord(text[i])
    store[temp].append(i)
que = [0]
dist = [0] * v
vis = [False] * v
vis[0] = True
while(len(que)):
    index = que.pop(0)
    if index == v - 1:
        break
    temp = ord(text[index])
    for i in store[temp]:
        if not vis[i]:
            vis[i] = True
            que.append(i)
            dist[i] = dist[index] + 1
    del store[temp]
    left = index - 1
    right = index + 1
    if left >= 0 and not vis[left]:
        vis[left] = True
        que.append(left)
        dist[left] = dist[index] + 1
    if right < v and not vis[right]:
        vis[right] = True
        que.append(right)
        dist[right] = dist[index] + 1
print(dist[v - 1])
