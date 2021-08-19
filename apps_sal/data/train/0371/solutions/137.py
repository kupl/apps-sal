class Solution:

    def numBusesToDestination(self, bus: List[List[int]], S: int, T: int) -> int:
        stop = collections.defaultdict(set)
        for (i, r) in enumerate(bus):
            for s in r:
                stop[s].add(i)
        q = collections.deque()
        q.append(S)
        visited = {S: 0}
        while q:
            cur = q.popleft()
            if cur == T:
                return visited[cur]
            for b in stop[cur]:
                for nxt in bus[b]:
                    if nxt not in visited:
                        visited[nxt] = visited[cur] + 1
                        q.append(nxt)
        return -1
