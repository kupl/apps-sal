'''input
5
-1 0
1 1
1 1
2 0
3 0
'''
from sys import stdin, stdout
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(15000)


def bfs(graph, parent, n):
    myq = deque()
    myq.append([parent, 0])
    ans = []
    while len(myq) != 0:
        node = myq.popleft()
        flag = 0
        for i in graph[node[0]]:
            myq.append(i)
            if i[1] == 1:
                continue
            else:
                flag = 1
        if flag == 0 and node[1] == 1:
            ans.append(node[0])
    return ans


# main starts
n = int(stdin.readline().strip())
graph = defaultdict(list)
parent = -1
for i in range(1, n + 1):
    node, key = list(map(int, stdin.readline().split()))
    if node == -1:
        parent = i
        continue
    graph[node].append([i, key])
# print(graph)
ans = bfs(graph, parent, n)
ans.sort()
if len(ans) > 0:
    print(*ans)
else:
    print(-1)
