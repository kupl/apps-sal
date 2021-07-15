from collections import deque
n, m = list(map(int, input().split()))
adjacent_list = [[] for i in range(3*n + 3)]
for i in range(m):
    u, v = list(map(int, input().split()))
    for j in range(1,4):
        p = j + 3 * u - 3
        q = (j % 3) + 3 * v - 2
        #print("{} -> {}".format(p, q))
        adjacent_list[p].append(q)
s, t = list(map(int, input().split()))

def bfs(start, target):
    que = deque()
    finished = set()
    que.append([start, 0])
    while que:
        node, dist = que.popleft()
        if (node, dist % 3) in finished:
            continue
        if node == target:
            return dist // 3
        for i in adjacent_list[node]:
            que.append([i, dist+1])
            finished.add((node, dist % 3))
    return -1
print((bfs(s*3 -2, 3*t-2)))


