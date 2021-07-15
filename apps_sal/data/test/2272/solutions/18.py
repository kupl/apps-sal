from collections import deque
from sys import stdin

N = int(stdin.readline().rstrip())
nodes = []
adj_list = []
for n in range(0, N):
    type, a, b = map(int, stdin.readline().rstrip().split())
    if type == 1:
        adj_list.append([])
        for index in range(0, len(nodes)):
            (c, d) = nodes[index]
            if c < a < d or c < b < d:
                adj_list[len(nodes)].append(index)
            if a < c < b or a < d < b:
                adj_list[index].append(len(nodes))
        nodes.append((a, b))
    else:
        queue = deque()
        visited = [False] * len(nodes)
        a -= 1
        b -= 1
        queue.append(a)
        path = False
        while queue:
            c = queue.popleft()
            if c == b:
                path = True
                break
            else:
                for d in adj_list[c]:
                    if not visited[d]:
                        queue.append(d)
                        visited[d] = True
        if path:
            print('YES')
        else:
            print('NO')
