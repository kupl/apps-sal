from queue import deque


def bfs(adjList, s, t):
    END = '$'
    queue = deque([s, END])
    visited = set()
    step = 0
    while queue:
        node = queue.popleft()
        if node == t:
            return step
        if node == END:
            if not queue:
                break
            step += 1
            queue.append(END)
            continue
        visited.add(node)
        for adjNode in adjList[node]:
            if adjNode not in visited:
                queue.append(adjNode)
    return -1


def numBusesToDestination_Graph_TLE(routes, S, T):
    adjList = {}
    for route in routes:
        for i in range(len(route)):
            if route[i] not in adjList:
                adjList[route[i]] = set()
            for j in range(i + 1, len(route)):
                if route[j] not in adjList:
                    adjList[route[j]] = set()
                adjList[route[i]].add(route[j])
                adjList[route[j]].add(route[i])
    if S not in adjList:
        return -1
    return bfs(adjList, S, T)


def numBusesToDestination_GraphTakeRouteAsNod_TLE(routes, S, T):
    if S == T:
        return 0
    adjList = {'S': [], 'T': []}
    for i in range(len(routes)):
        routes[i] = set(routes[i])
        adjList[i] = []
        if S in routes[i]:
            adjList['S'].append(i)
        if T in routes[i]:
            adjList[i].append('T')
    for i in range(len(routes)):
        for j in range(i + 1, len(routes)):
            if any([k in routes[j] for k in routes[i]]):
                adjList[i].append(j)
                adjList[j].append(i)
    return max(bfs(adjList, 'S', 'T') - 1, -1)


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        return numBusesToDestination_GraphTakeRouteAsNod_TLE(routes, S, T)
